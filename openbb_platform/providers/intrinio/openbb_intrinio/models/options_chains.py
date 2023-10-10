"""Intrinio Options Chains fetcher."""

from concurrent.futures import ThreadPoolExecutor
from datetime import (
    date as dateType,
    datetime,
    timedelta,
)
from itertools import repeat
from typing import Any, Dict, List, Optional

from openbb_intrinio.utils.helpers import get_data_many
from openbb_intrinio.utils.references import TICKER_EXCEPTIONS
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.options_chains import (
    OptionsChainsData,
    OptionsChainsQueryParams,
)
from pydantic import Field, validator


class IntrinioOptionsChainsQueryParams(OptionsChainsQueryParams):
    """Get the complete options chains (Historical) for a ticker from Intrinio.

    source: https://docs.intrinio.com/documentation/web_api/get_options_chain_eod_v2
    """

    date: Optional[dateType] = Field(
        description="Date for which the options chains are returned."
    )


class IntrinioOptionsChainsData(OptionsChainsData):
    """Intrinio Options Chains Data."""

    __alias_dict__ = {"contract_symbol": "code", "symbol": "ticker"}

    @validator("expiration", "date", pre=True, check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string"""
        return datetime.strptime(v, "%Y-%m-%d")


def get_weekday(date: dateType) -> str:
    """Return the weekday date."""
    if date.weekday() in [5, 6]:
        return (date - timedelta(days=date.weekday() - 4)).strftime("%Y-%m-%d")
    return date.strftime("%Y-%m-%d")


class IntrinioOptionsChainsFetcher(
    Fetcher[IntrinioOptionsChainsQueryParams, List[IntrinioOptionsChainsData]]
):
    """Perform TET for the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioOptionsChainsQueryParams:
        """Transform the query."""
        transform_params = params

        now = datetime.now().date()
        if params.get("date") is None:
            transform_params["date"] = (now - timedelta(days=1)).strftime("%Y-%m-%d")

        return IntrinioOptionsChainsQueryParams(**transform_params)

    @staticmethod
    def extract_data(
        query: IntrinioOptionsChainsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

        if query.symbol in TICKER_EXCEPTIONS:
            query.symbol = f"${query.symbol}"

        data: List = []
        base_url = "https://api-v2.intrinio.com/options"

        def get_expirations(date: str) -> List[str]:
            """Return the expirations for the given date."""
            url = (
                f"{base_url}/expirations/{query.symbol}/eod?"
                f"after={date}&api_key={api_key}"
            )
            return get_data_many(url, "expirations", **kwargs)

        def get_options_chains(
            expiration: str, data: List[IntrinioOptionsChainsData]
        ) -> None:
            """Return the data for the given expiration."""
            url = (
                f"{base_url}/chain/{query.symbol}/{expiration}/eod?"
                f"date={query.date}&api_key={api_key}"
            )
            response = get_data_many(url, "chain", **kwargs)
            data.extend(response)

        def get_data(date: str) -> None:
            """Fetch data for a given date using ThreadPoolExecutor."""
            expirations = get_expirations(date)
            with ThreadPoolExecutor() as executor:
                executor.map(get_options_chains, expirations, repeat(data))

        date = get_weekday(query.date)
        get_data(date)

        if not data:
            date = get_weekday(query.date - timedelta(days=1))
            get_data(date)

        return data

    @staticmethod
    def transform_data(data: List[Dict]) -> List[IntrinioOptionsChainsData]:
        """Return the transformed data."""
        data = [{**item["option"], **item["prices"]} for item in data]
        return [IntrinioOptionsChainsData.model_validate(d) for d in data]

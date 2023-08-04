"""yfinance Crypto end of day fetcher."""


from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_provider.models.crypto_eod import CryptoEODData, CryptoEODQueryParams
from pydantic import Field, validator
from yfinance import Ticker

from openbb_yfinance.utils.types import INTERVALS, PERIODS


class YFinanceCryptoEODQueryParams(CryptoEODQueryParams):
    """YFinance Crypto end of day Query.

    Source: https://finance.yahoo.com/crypto/
    """

    interval: Optional[INTERVALS] = Field(default="1d", description="Data granularity.")
    period: Optional[PERIODS] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("period", "")
    )


class YFinanceCryptoEODData(CryptoEODData):
    """YFinance Crypto end of day Data."""

    class Config:
        fields = {
            "date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume",
        }

    @validator("Date", pre=True, check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")


class YFinanceCryptoEODFetcher(
    Fetcher[
        CryptoEODQueryParams,
        CryptoEODData,
        YFinanceCryptoEODQueryParams,
        YFinanceCryptoEODData,
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFinanceCryptoEODQueryParams:
        now = datetime.now().date()
        transformed_params = params
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - timedelta(days=7)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now
        return YFinanceCryptoEODQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceCryptoEODQueryParams, credentials: Optional[Dict[str, str]]
    ) -> List[YFinanceCryptoEODData]:
        now = datetime.now().date()
        query.start_date = query.start_date or (now - timedelta(days=8))
        query.end_date = query.end_date or (now - timedelta(days=1))

        if query.period:
            data = Ticker(query.symbol).history(
                interval=query.interval,
                period=query.period,
                actions=False,
                raise_errors=True,
            )
        else:
            data = Ticker(query.symbol).history(
                interval=query.interval,
                start=query.start_date,
                end=query.end_date,
                actions=False,
                raise_errors=True,
            )

        data = data.reset_index()
        data["Date"] = (
            data["Date"].dt.tz_localize(None).dt.strftime("%Y-%m-%dT%H:%M:%S")
        )
        data = data.to_dict("records")

        return [YFinanceCryptoEODData(**d) for d in data]

    @staticmethod
    def transform_data(
        data: List[YFinanceCryptoEODData],
    ) -> List[YFinanceCryptoEODData]:
        return data

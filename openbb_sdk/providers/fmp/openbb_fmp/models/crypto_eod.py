"""FMP Cryptos end of day fetcher."""


from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.crypto_eod import (
    CryptoEODData,
    CryptoEODQueryParams,
)
from openbb_provider.utils.helpers import get_querystring
from pydantic import Field, NonNegativeInt, validator

from openbb_fmp.utils.helpers import get_data_many


class FMPCryptoEODQueryParams(CryptoEODQueryParams):
    """FMP Crypto end of day Query.

    Source: https://site.financialmodelingprep.com/developer/docs/cryptocurrency-historical-data-api/#Historical-Daily-Prices
    """

    timeseries: Optional[NonNegativeInt] = Field(
        default=None, description="Number of days to look back."
    )


class FMPCryptoEODData(CryptoEODData):
    """FMP Crypto end of day Data."""

    adjClose: float = Field(
        description="Adjusted Close Price of the symbol.", alias="adj_close"
    )
    unadjustedVolume: float = Field(
        description="Unadjusted volume of the symbol.", alias="unadjusted_volume"
    )
    change: float = Field(
        description="Change in the price of the symbol from the previous day.",
        alias="change",
    )
    changePercent: float = Field(
        description=r"Change \% in the price of the symbol.", alias="change_percent"
    )
    label: str = Field(description="Human readable format of the date.")
    changeOverTime: float = Field(
        description=r"Change \% in the price of the symbol over a period of time.",
        alias="change_over_time",
    )

    @validator("date", pre=True)
    def date_validate(cls, v):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%d")


class FMPCryptoEODFetcher(
    Fetcher[
        FMPCryptoEODQueryParams,
        FMPCryptoEODData,
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCryptoEODQueryParams:
        now = datetime.now().date()
        transformed_params = params
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - timedelta(days=7)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now
        return FMPCryptoEODQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: FMPCryptoEODQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[FMPCryptoEODData]:
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3/"
        query_str = get_querystring(query.dict(by_alias=True), ["symbol"])
        query_str = query_str.replace("start_date", "from").replace("end_date", "to")
        url = f"{base_url}historical-price-full/crypto/{query.symbol}?{query_str}&apikey={api_key}"

        return get_data_many(url, FMPCryptoEODData, "historical", **kwargs)

    @staticmethod
    def transform_data(data: List[FMPCryptoEODData]) -> List[FMPCryptoEODData]:
        return data

"""FMP Stock Insider Trading fetcher."""


from typing import Any, Dict, List, Optional

from openbb_provider.utils.helpers import get_querystring
from openbb_fmp.utils.helpers import create_url, get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_insider_trading import (
    StockInsiderTradingData,
    StockInsiderTradingQueryParams,
)


class FMPStockInsiderTradingQueryParams(StockInsiderTradingQueryParams):
    """FMP Stock Insider Trading Query.

    Source: https://site.financialmodelingprep.com/developer/docs/#Stock-Insider-Trading
    """


class FMPStockInsiderTradingData(StockInsiderTradingData):
    """FMP Stock Insider Trading Data."""

    __alias_dict__ = {
        "acquisition_or_disposition": "acquistionOrDisposition",
        "last_number_of_13f_shares": "lastNumberOf13FShares",
    }


class FMPStockInsiderTradingFetcher(
    Fetcher[
        FMPStockInsiderTradingQueryParams,
        List[FMPStockInsiderTradingData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPStockInsiderTradingQueryParams:
        """Transform the query params."""
        return FMPStockInsiderTradingQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPStockInsiderTradingQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v4/insider-trading"
        query_str = get_querystring(query.model_dump(by_alias=True), ["page"])

        data: List[Dict] = []

        for page in range(4):
            url = f"{base_url}?{query_str}&page={page}&apikey={api_key}"
            data.extend(get_data_many(url, **kwargs))

        return data


    @staticmethod
    def transform_data(data: List[Dict]) -> List[FMPStockInsiderTradingData]:
        """Return the transformed data."""
        data = [FMPStockInsiderTradingData.model_validate(d) for d in data]
        return sorted(data, key=lambda x: x.filing_date, reverse=True)

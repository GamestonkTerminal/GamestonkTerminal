"""FMP Stock News fetcher."""


from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.models.stock_news import StockNewsData, StockNewsQueryParams
from pydantic import Field

from openbb_fmp.utils.helpers import create_url, get_data_many


class FMPStockNewsQueryParams(StockNewsQueryParams):
    """FMP Stock News query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-news-api/
    """

    class Config:
        fields = {"symbols": "tickers"}


class FMPStockNewsData(Data):
    symbol: str
    publishedDate: datetime = Field(alias="date")
    title: str
    image: Optional[str]
    text: str
    url: str
    site: str


class FMPStockNewsFetcher(
    Fetcher[
        StockNewsQueryParams,
        StockNewsData,
        FMPStockNewsQueryParams,
        FMPStockNewsData,
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPStockNewsQueryParams:
        return FMPStockNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPStockNewsQueryParams, credentials: Optional[Dict[str, str]]
    ) -> List[FMPStockNewsData]:
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(3, "stock_news", api_key, query)
        return get_data_many(url, FMPStockNewsData)

    @staticmethod
    def transform_data(data: List[FMPStockNewsData]) -> List[FMPStockNewsData]:
        return data

"""intrinio provider module."""


from openbb_provider.abstract.provider import Provider

from openbb_intrinio.models.stock_eod import IntrinioStockEODFetcher
from openbb_intrinio.models.stock_news import IntrinioStockNewsFetcher
from openbb_intrinio.models.forex_pairs import IntrinioForexPairsFetcher
from openbb_intrinio.models.global_news import IntrinioGlobalNewsFetcher

intrinio_provider = Provider(
    name="intrinio",
    website="https://intrinio.com/",
    description="""Intrinio is a financial data platform that provides real-time and
    historical financial market data to businesses and developers through an API.""",
    required_credentials=["api_key"],
    fetcher_dict={
        "StockEOD": IntrinioStockEODFetcher,
        "ForexPairs": IntrinioForexPairsFetcher,
        "StockNews": IntrinioStockNewsFetcher,
        "GlobalNews": IntrinioGlobalNewsFetcher,
    },
)

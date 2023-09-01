"""Alpha Vantage Provider module."""
from openbb_provider.abstract.provider import Provider

from openbb_alpha_vantage.models.stock_eod import AVStockEODFetcher

alpha_vantage_provider = Provider(
    name="alpha_vantage",
    website="https://www.alphavantage.co/documentation/",
    description="""Alpha Vantage provides realtime and historical
    financial market data through a set of powerful and developer-friendly data APIs
    and spreadsheets. From traditional asset classes (e.g., stocks, ETFs, mutual funds)
    to economic indicators, from foreign exchange rates to commodities,
    from fundamental data to technical indicators, Alpha Vantage
    is your one-stop-shop for enterprise-grade global market data delivered through
    cloud-based APIs, Excel, and Google Sheets. """,
    required_credentials=["api_key"],
    fetcher_dict={
        "StockEOD": AVStockEODFetcher,
    },
)

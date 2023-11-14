"""Tiingo provider module."""

from openbb_provider.abstract.provider import Provider
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.global_news import TiingoGlobalNewsFetcher

tiingo_provider = Provider(
    name="tiingo",
    website="https://tiingo.com/",
    description="""""",
    required_credentials=["token"],
    fetcher_dict={
        "EquityHistorical": TiingoEquityHistoricalFetcher,
        "CompanyNews": TiingoCompanyNewsFetcher,
        "GlobalNews": TiingoGlobalNewsFetcher,
        "CryptoHistorical": TiingoCryptoHistoricalFetcher,
    },
)

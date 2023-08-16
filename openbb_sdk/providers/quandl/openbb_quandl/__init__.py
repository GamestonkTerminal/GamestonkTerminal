"""quandl provider module."""
from openbb_provider.abstract.provider import Provider

from openbb_quandl.models.sp500_multiples import QuandlSP500MultiplesFetcher

quandl_provider = Provider(
    name="quandl",
    website="data.nasdaq.com/publishers/qdl",
    description="""Quandl is a premier publisher of alternative data for institutional investors.
    A dedicated team of data scientists, quants and engineers combine uncompromising curation,
    high quality standards and experienced data science application to provide some of the most powerful data available
    today. Quandl also publishes free data, scraped from the web and delivered via Nasdaq Data Link's
    industry-leading data delivery platform.
    """,
    required_credentials=["api_key"],
    fetcher_dict={"SP500Multiples": QuandlSP500MultiplesFetcher},
)

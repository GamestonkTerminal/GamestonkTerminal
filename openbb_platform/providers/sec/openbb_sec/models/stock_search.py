"""SEC Company Search fetcher."""


from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_search import (
    StockSearchData,
    StockSearchQueryParams,
)
from openbb_sec.utils.helpers import (
    get_all_companies,
    get_mf_and_etf_map,
    search_institutions,
)
from pandas import DataFrame
from pydantic import Field


class SecStockSearchQueryParams(StockSearchQueryParams):
    """SEC Company or Institution Search query.  This function assists with mapping the CIK number to a company.

    Source: https://sec.gov/
    """

    is_fund: bool = Field(
        default=False,
        description="Whether to direct the search to the list of mutual funds and ETFs.",
    )
    is_institution: bool = Field(
        default=False,
        description="Whether to direct the search to the list of institutions.",
    )
    use_cache: bool = Field(
        default=True,
        description="Whether to use the cache or not. Company names, tickers, and CIKs are cached for seven days.",
    )


class SecStockSearchData(StockSearchData):
    """SEC Company Search Data."""

    name: Optional[str] = Field(default=None)
    cik: str = Field(description="Central Index Key")


class SecStockSearchFetcher(
    Fetcher[
        SecStockSearchQueryParams,
        List[SecStockSearchData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SecStockSearchQueryParams:
        """Transform the query."""
        return SecStockSearchQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecStockSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the SEC endpoint."""

        results = DataFrame()

        if query.is_fund is True:
            companies = get_mf_and_etf_map(use_cache=query.use_cache).astype(str)
            results = companies[
                companies["cik"].str.contains(query.query, case=False)
                | companies["seriesId"].str.contains(query.query, case=False)
                | companies["classId"].str.contains(query.query, case=False)
                | companies["symbol"].str.contains(query.query, case=False)
            ]

        if query.is_fund is False and query.is_institution is False:
            companies = get_all_companies(use_cache=query.use_cache)

            results = companies[
                companies["name"].str.contains(query.query, case=False)
                | companies["symbol"].str.contains(query.query, case=False)
                | companies["cik"].str.contains(query.query, case=False)
            ]

        if query.is_institution is True:
            results = search_institutions(query.query, use_cache=query.use_cache)

        return results.astype(str).to_dict("records")

    @staticmethod
    def transform_data(data: Dict, **kwargs: Any) -> List[SecStockSearchData]:
        """Transform the data to the standard format."""
        return [SecStockSearchData.model_validate(d) for d in data]

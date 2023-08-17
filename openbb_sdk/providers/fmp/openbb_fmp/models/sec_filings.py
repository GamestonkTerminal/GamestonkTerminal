"""SEC Filings fetcher."""


from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.sec_filings import (
    SECFilingsData,
    SECFilingsQueryParams,
)

from openbb_fmp.utils.helpers import create_url, get_data_many


class FMPSECFilingsQueryParams(SECFilingsQueryParams):
    """FMP SEC Filings Query.

    Source: https://site.financialmodelingprep.com/developer/docs/sec-filings-api/
    """


class FMPSECFilingsData(SECFilingsData):
    """FMP SEC Filings Data."""

    class Config:
        fields = {
            "filling_date": "fillingDate",
            "accepted_date": "acceptedDate",
            "final_link": "finalLink",
        }


class FMPSECFilingsFetcher(
    Fetcher[
        FMPSECFilingsQueryParams,
        List[FMPSECFilingsData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPSECFilingsQueryParams:
        return FMPSECFilingsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPSECFilingsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"sec_filings/{query.symbol}", api_key, query, exclude=["symbol"]
        )

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(data: List[dict]) -> List[FMPSECFilingsData]:
        return [FMPSECFilingsData(**d) for d in data]

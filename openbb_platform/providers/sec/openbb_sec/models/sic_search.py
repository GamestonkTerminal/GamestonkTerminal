"""SEC Standard Industrial Classification Code (SIC) Model."""

# pylint: disable=unused-argument

from typing import Any, Dict, List, Optional

import pandas as pd
from aiohttp_client_cache import SQLiteBackend
from aiohttp_client_cache.session import CachedSession
from openbb_core.app.utils import get_user_cache_directory
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cot_search import CotSearchQueryParams
from openbb_core.provider.utils.helpers import amake_request
from openbb_sec.utils.helpers import SEC_HEADERS, sec_callback
from pydantic import Field


class SecSicSearchQueryParams(CotSearchQueryParams):
    """SEC Standard Industrial Classification Code (SIC) Query.

    Source: https://sec.gov/
    """


class SecSicSearchData(Data):
    """SEC Standard Industrial Classification Code (SIC) Data."""

    sic: int = Field(description="Sector Industrial Code (SIC)", alias="SIC Code")
    industry: str = Field(description="Industry title.", alias="Industry Title")
    office: str = Field(
        description="Reporting office within the Corporate Finance Office",
        alias="Office",
    )


class SecSicSearchFetcher(
    Fetcher[
        SecSicSearchQueryParams,
        List[SecSicSearchData],
    ]
):
    """Transform the query, extract and transform the data from the SEC endpoints."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any], **kwargs: Any
    ) -> SecSicSearchQueryParams:
        """Transform the query."""
        return SecSicSearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SecSicSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract data from the SEC website table."""
        data = pd.DataFrame()
        results: List[Dict] = []
        url = (
            "https://www.sec.gov/corpfin/"
            "division-of-corporation-finance-standard-industrial-classification-sic-code-list"
        )
        if query.use_cache is True:
            cache_dir = f"{get_user_cache_directory()}/http/sec_sic"
            async with CachedSession(
                cache=SQLiteBackend(cache_dir, expire_after=3600 * 24 * 30)
            ) as session:
                try:
                    response = await amake_request(
                        url, headers=SEC_HEADERS, session=session, response_callback=sec_callback  # type: ignore
                    )
                finally:
                    await session.close()
        else:
            response = await amake_request(url, headers=SEC_HEADERS, response_callback=sec_callback)  # type: ignore

        data = pd.read_html(response)[0].astype(str)
        if len(data) == 0:
            return results
        if query:
            data = data[
                data["SIC Code"].str.contains(query.query, case=False)
                | data["Office"].str.contains(query.query, case=False)
                | data["Industry Title"].str.contains(query.query, case=False)
            ]
        data["SIC Code"] = data["SIC Code"].astype(int)
        results = data.to_dict("records")

        return results

    @staticmethod
    def transform_data(
        query: SecSicSearchQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[SecSicSearchData]:
        """Transform the data."""
        return [SecSicSearchData.model_validate(d) for d in data]

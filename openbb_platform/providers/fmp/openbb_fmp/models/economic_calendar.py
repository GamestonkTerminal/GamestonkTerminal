"""FMP Economic Calendar Model."""

# pylint: disable=unused-argument

import asyncio
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.economic_calendar import (
    EconomicCalendarData,
    EconomicCalendarQueryParams,
)
from openbb_core.provider.utils.helpers import amake_request
from pydantic import Field, field_validator, model_validator


class FMPEconomicCalendarQueryParams(EconomicCalendarQueryParams):
    """FMP Economic Calendar Query.

    Source: https://site.financialmodelingprep.com/developer/docs/economic-calendar-api
    """


class FMPEconomicCalendarData(EconomicCalendarData):
    """FMP Economics Calendar Data.

    Source: https://site.financialmodelingprep.com/developer/docs/economic-calendar-api
    """

    __alias_dict__ = {
        "consensus": "estimate",
        "importance": "impact",
        "last_updated": "updatedAt",
        "created_at": "createdAt",
        "change_percent": "changePercentage",
    }

    change: Optional[float] = Field(
        description="Value change since previous.",
        default=None,
    )
    change_percent: Optional[float] = Field(
        description="Percentage change since previous.",
        default=None,
    )
    last_updated: Optional[datetime] = Field(
        description="Last updated timestamp.", default=None
    )
    created_at: Optional[datetime] = Field(
        description="Created at timestamp.", default=None
    )

    @field_validator(
        "date", "last_updated", "created_at", mode="before", check_fields=False
    )
    def date_validate(cls, v: str):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d %H:%M:%S") if v else None

    @model_validator(mode="before")
    @classmethod
    def empty_strings(cls, values):
        """Replace empty values with None."""
        return (
            {k: (None if v in ("", 0) else v) for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )


class FMPEconomicCalendarFetcher(
    Fetcher[
        FMPEconomicCalendarQueryParams,
        List[FMPEconomicCalendarData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEconomicCalendarQueryParams:
        """Transform the query."""
        return FMPEconomicCalendarQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEconomicCalendarQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3/economic_calendar?"

        # FMP allows only 3-month windows to be queried, we need to chunk to request.
        if not query.start_date or query.start_date is None:
            query.start_date = datetime.now().date()
        if not query.end_date or query.end_date is None:
            query.end_date = (datetime.now() + timedelta(days=7)).date()

        def date_range(start_date, end_date):
            """Yield start and end dates for each 90-day period between start_date and end_date."""
            delta = timedelta(days=90)
            current_date = start_date
            while current_date < end_date:
                next_date = min(current_date + delta, end_date)
                yield current_date, next_date
                current_date = next_date + timedelta(days=1)

        date_ranges = [
            (start, end) for start, end in date_range(query.start_date, query.end_date)
        ]
        urls = [
            f"{base_url}from={start_date.strftime('%Y-%m-%d')}&to={end_date.strftime('%Y-%m-%d')}&apikey={api_key}"
            for start_date, end_date in date_ranges
        ]
        results: List[Dict] = []

        # We need to do this because Pytest does not seem to be able to handle amake_requests`.
        async def get_one(url):
            """Get data for one URL."""
            n_urls = 1
            try:
                result = await amake_request(url, **kwargs)
                if result:
                    results.extend(result)
            except Exception as e:
                if len(urls) == 1 or (len(urls) > 1 and n_urls == len(urls)):
                    raise e from e
                else:
                    warn(f"Error in fetching part of the data from FMP -> {e}")

        await asyncio.gather(*[get_one(url) for url in urls])

        return results

    @staticmethod
    def transform_data(
        query: FMPEconomicCalendarQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[FMPEconomicCalendarData]:
        """Transform the data."""
        return [FMPEconomicCalendarData.model_validate(d) for d in data]

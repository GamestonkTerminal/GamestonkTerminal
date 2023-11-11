"""FMP Historical EPS fetcher."""


from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Optional

from openbb_fmp.utils.helpers import create_url, get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.historical_eps import (
    HistoricalEpsData,
    HistoricalEpsQueryParams,
)
from pydantic import Field, field_validator


class FMPHistoricalEpsQueryParams(HistoricalEpsQueryParams):
    """FMP Historical EPS Query.

    Source: https://site.financialmodelingprep.com/developer/docs/earnings-calendar-api/
    """


class FMPHistoricalEpsData(HistoricalEpsData):
    """FMP Historical EPS Data."""

    actual_eps: Optional[float] = Field(
        default=None,
        description="The actual earnings per share announced.",
        alias="eps",
    )
    revenue_estimated: Optional[float] = Field(
        default=None,
        description="Estimated consensus revenue for the reporting period.",
        alias="revenueEstimated",
    )
    actual_revenue: Optional[float] = Field(
        default=None,
        description="The actual reported revenue.",
        alias="revenue",
    )
    reporting_time: Optional[str] = Field(
        default=None,
        description="The reporting time - e.g. after market close.",
        alias="time",
    )
    updated_at: Optional[dateType] = Field(
        default=None,
        description="The date when the data was last updated.",
        alias="updatedFromDate",
    )
    period_ending: Optional[dateType] = Field(
        default=None,
        description="The fiscal period end date.",
        alias="fiscalDateEnding",
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v: str):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d") if v else None

    @field_validator("updatedFromDate", mode="before", check_fields=False)
    def updated_from_date_validate(cls, v: str):  # pylint: disable=E0213
        """Return the updated from date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d") if v else None

    @field_validator("fiscalDateEnding", mode="before", check_fields=False)
    def fiscal_date_ending_validate(cls, v: str):  # pylint: disable=E0213
        """Return the fiscal date ending as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d") if v else None


class FMPHistoricalEpsFetcher(
    Fetcher[
        FMPHistoricalEpsQueryParams,
        List[FMPHistoricalEpsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPHistoricalEpsQueryParams:
        """Transform the query params."""
        return FMPHistoricalEpsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPHistoricalEpsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        url = create_url(
            3, f"historical/earning_calendar/{query.symbol}", api_key, query, ["symbol"]
        )

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPHistoricalEpsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPHistoricalEpsData]:
        """Return the transformed data."""
        return [FMPHistoricalEpsData.model_validate(d) for d in data]

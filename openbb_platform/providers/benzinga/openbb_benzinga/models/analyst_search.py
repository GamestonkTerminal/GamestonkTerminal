"""Benzinga Analyst Search Model."""

# pylint: disable=unused-argument

from datetime import (
    date as dateType,
    timezone,
)
from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.analyst_search import (
    AnalystSearchData,
    AnalystSearchQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import (
    amake_request,
    get_querystring,
    safe_fromtimestamp,
)
from pydantic import Field, field_validator, model_validator


class BenzingaAnalystSearchQueryParams(AnalystSearchQueryParams):
    """Benzinga Analyst Search Query.

    Source: https://docs.benzinga.io/benzinga-apis/calendar/get-analysts
    """

    __alias_dict__ = {
        "analyst_ids": "analyst",
        "firm_ids": "firm",
        "limit": "pageSize",
    }
    __json_schema_extra__ = {
        "analyst_name": ["multiple_items_allowed"],
        "firm_name": ["multiple_items_allowed"],
        "analyst_ids": ["multiple_items_allowed"],
        "firm_ids": ["multiple_items_allowed"],
        "fields": ["multiple_items_allowed"],
    }

    analyst_ids: Optional[str] = Field(
        default=None,
        description="List of analyst IDs to return.",
    )
    firm_ids: Optional[str] = Field(
        default=None,
        description="Firm IDs to return.",
    )
    limit: Optional[int] = Field(
        default=100,
        description="Number of results returned. Limit 1000.",
    )
    page: Optional[int] = Field(
        default=0,
        description="Page offset. For optimization,"
        + " performance and technical reasons, page offsets"
        + " are limited from 0 - 100000."
        + " Limit the query results by other parameters such as date.",
    )
    fields: Optional[str] = Field(
        default=None,
        description="Fields to include in the response."
        " See https://docs.benzinga.io/benzinga-apis/calendar/get-ratings to learn about the available fields.",
    )


class BenzingaAnalystSearchData(AnalystSearchData):
    """Benzinga Analyst Search Data."""

    __alias_dict__ = {
        "analyst_id": "id",
        "last_updated": "updated",
    }
    analyst_id: Optional[str] = Field(
        default=None,
        description="ID of the analyst.",
    )
    firm_id: Optional[str] = Field(
        default=None,
        description="ID of the analyst firm.",
    )
    smart_score: Optional[float] = Field(
        default=None,
        description="A weighted average of the total_ratings_percentile,"
        + " overall_avg_return_percentile, and overall_success_rate",
    )
    overall_success_rate: Optional[float] = Field(
        default=None,
        description="The percentage (normalized) of gain/loss ratings that resulted in a gain overall.",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
    )
    overall_avg_return_percentile: Optional[float] = Field(
        default=None,
        description="The percentile (normalized) of this analyst's overall average"
        + " return per rating in comparison to other analysts' overall average returns per rating.",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
    )
    total_ratings_percentile: Optional[float] = Field(
        default=None,
        description="The percentile (normalized) of this analyst's total number of ratings"
        + " in comparison to the total number of ratings published by all other analysts",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
    )
    total_ratings: Optional[int] = Field(
        default=None,
        description="Number of recommendations made by this analyst.",
    )
    overall_gain_count: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value since the date of recommendation",
    )
    overall_loss_count: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value since the date of recommendation",
    )
    overall_average_return: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating since the date of recommendation",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
    )
    overall_std_dev: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings since the date of recommendation",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="overall_stdev",
    )
    gain_count_1m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last month",
        alias="1m_gain_count",
    )
    loss_count_1m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last month",
        alias="1m_loss_count",
    )
    average_return_1m: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over the last month",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="1m_average_return",
    )
    std_dev_1m: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last month",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="1m_stdev",
    )
    gain_count_3m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 3 months",
        alias="3m_gain_count",
    )
    loss_count_3m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 3 months",
        alias="3m_loss_count",
    )
    average_return_3m: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 3 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="3m_average_return",
    )
    std_dev_3m: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 3 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="3m_stdev",
    )
    gain_count_6m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 6 months",
        alias="6m_gain_count",
    )
    loss_count_6m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 6 months",
        alias="6m_loss_count",
    )
    average_return_6m: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 6 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="6m_average_return",
    )
    std_dev_6m: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 6 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="6m_stdev",
    )
    gain_count_9m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 9 months",
        alias="9m_gain_count",
    )
    loss_count_9m: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 9 months",
        alias="9m_loss_count",
    )
    average_return_9m: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 9 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="9m_average_return",
    )
    std_dev_9m: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 9 months",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="9m_stdev",
    )
    gain_count_1y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 1 year",
        alias="1y_gain_count",
    )
    loss_count_1y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 1 year",
        alias="1y_loss_count",
    )
    average_return_1y: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 1 year",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="1y_average_return",
    )
    std_dev_1y: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 1 year",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="1y_stdev",
    )
    gain_count_2y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 2 years",
        alias="2y_gain_count",
    )
    loss_count_2y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 2 years",
        alias="2y_loss_count",
    )
    average_return_2y: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 2 years",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="2y_average_return",
    )
    std_dev_2y: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 2 years",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="2y_stdev",
    )
    gain_count_3y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have gained value over the last 3 years",
        alias="3y_gain_count",
    )
    loss_count_3y: Optional[int] = Field(
        default=None,
        description="The number of ratings that have lost value over the last 3 years",
        alias="3y_loss_count",
    )
    average_return_3y: Optional[float] = Field(
        default=None,
        description="The average percent (normalized) price difference per rating over"
        + " the last 3 years",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="3y_average_return",
    )
    std_dev_3y: Optional[float] = Field(
        default=None,
        description="The standard deviation in percent (normalized) price difference in the"
        + " analyst's ratings over the last 3 years",
        json_schema_extra={"unit_measurement": "percent", "frontend_multiply": 100},
        alias="3y_stdev",
    )

    @field_validator("last_updated", mode="before", check_fields=False)
    @classmethod
    def validate_date(cls, v: float) -> Optional[dateType]:
        """Validate last_updated."""
        if v:
            dt = safe_fromtimestamp(v, tz=timezone.utc)
            return dt.date() if dt.time() == dt.min.time() else dt
        return v

    @model_validator(mode="before")
    @classmethod
    def replace_empty_strings(cls, values):
        """Check for empty strings and replace with None."""
        return (
            {k: None if v == "" else v for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )

    @model_validator(mode="before")
    @classmethod
    def normalize_percent(cls, values):
        """Normalize percent values."""
        contains = ["return", "percentile", "stdev", "rate"]
        for key in values:
            if any(x in key for x in contains):
                values[key] = (
                    float(values[key]) / 100
                    if values[key] != "" or values[key] is not None
                    else None
                )
        return values


class BenzingaAnalystSearchFetcher(
    Fetcher[BenzingaAnalystSearchQueryParams, List[BenzingaAnalystSearchData]]
):
    """Benzinga Analyst Search Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> BenzingaAnalystSearchQueryParams:
        """Transform query params."""
        return BenzingaAnalystSearchQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: BenzingaAnalystSearchQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract the raw data."""
        token = credentials.get("benzinga_api_key") if credentials else ""
        querystring = get_querystring(query.model_dump(), [])
        url = f"https://api.benzinga.com/api/v2.1/calendar/ratings/analysts?{querystring}&token={token}"
        response = await amake_request(url, **kwargs)

        if not response:
            raise EmptyDataError()

        return response.get("analyst_ratings_analyst")  # type: ignore

    @staticmethod
    def transform_data(
        query: BenzingaAnalystSearchQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[BenzingaAnalystSearchData]:
        """Transform the data."""
        results: List[BenzingaAnalystSearchData] = []
        for item in data:
            if item.get("firm_id"):
                result = {
                    "updated": item.get("updated", None),
                    "firm_id": item.get("firm_id", None),
                    "firm_name": item.get("firm_name", None),
                    "id": item.get("id", None),
                    "name_first": item.get("name_first", None),
                    "name_full": item.get("name_full", None),
                    "name_last": item.get("name_last", None),
                    **item["ratings_accuracy"],
                }
                results.append(BenzingaAnalystSearchData.model_validate(result))
        return results

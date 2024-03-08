"""ETF Performance Standard Model."""

from datetime import date as dateType
from typing import Literal, Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class ETFPerformanceQueryParams(QueryParams):
    """ETF Performance Query."""

    sort: Literal["asc", "desc"] = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )
    limit: Optional[int] = Field(
        default=10,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )

    @field_validator("sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: Optional[str]) -> Optional[str]:
        """Convert field to lowercase."""
        return v.lower() if v else v


class ETFPerformanceData(Data):
    """ETF Performance Data."""

    date: Optional[dateType] = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("date", ""),
    )
    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: Optional[str] = Field(
        default=None,
        description="Name of the entity.",
    )
    price: float = Field(
        description="Last price.",
    )
    change: Optional[float] = Field(
        description="Change in price value.",
    )
    change_percent: Optional[float] = Field(
        default=None,
        description="Change in price as a normalized percentage.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volume: Optional[float] = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )

"""Calendar Splits Standard Model."""


from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class CalendarSplitsQueryParams(QueryParams):
    """Calendar Splits Query."""

    start_date: Optional[dateType] = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: Optional[dateType] = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )


class CalendarSplitsData(Data):
    """Calendar Splits Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", "") + " (Ex-date)")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    numerator: Optional[float] = Field(
        default=None, description="Numerator of the stock splits."
    )
    denominator: Optional[float] = Field(
        default=None, description="Denominator of the stock splits."
    )
    factor: Optional[float] = Field(default=None, description="The split factor value.")

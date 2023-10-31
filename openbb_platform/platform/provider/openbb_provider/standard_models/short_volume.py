"""Short Volume data and query params."""
from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class ShortVolumeQueryParams(QueryParams):
    """Short Volume query."""

    symbol: str = Field(default=None, description=QUERY_DESCRIPTIONS.get("symbol"))


class ShortVolumeData(Data):
    """Short Volume data."""

    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )

    market: Optional[str] = Field(
        default=None,
        description="Reporting Facility ID. N=NYSE TRF, Q=NASDAQ TRF Carteret, B=NASDAQ TRY Chicago, D=FINRA ADF",
    )

    short_volume: Optional[int] = Field(
        default=None,
        description="Aggregate reported share volume of executed short sale and short sale exempt trades during regular trading hours",
    )

    short_exempt_volume: Optional[int] = Field(
        default=None,
        description="Aggregate reported share volume of executed short sale exempt trades during regular trading hours",
    )

    total_volume: Optional[int] = Field(
        default=None,
        description="Aggregate reported share volume of executed trades during regular trading hours",
    )

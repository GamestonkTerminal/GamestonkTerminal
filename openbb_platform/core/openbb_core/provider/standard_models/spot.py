"""Spot Rate Standard Model."""

from datetime import (
    date as dateType,
)
from typing import List, Literal, Optional, Union

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class SpotRateQueryParams(QueryParams):
    """Spot Rate Query."""

    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Union[float, str] = Field(
        default=10.0, description="The maturities in years."
    )
    category: List[Literal["par_yield", "spot_rate"]] = Field(
        default=["spot_rate"],
        description="The category.",
    )


class SpotRateData(Data):
    """Spot Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: Optional[float] = Field(description="Spot Rate.")

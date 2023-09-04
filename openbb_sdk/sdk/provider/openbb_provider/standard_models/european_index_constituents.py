"""European Index Constituents data model."""


from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.standard_models.base import BaseSymbol
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS


class EuropeanIndexConstituentsQueryParams(QueryParams, BaseSymbol):
    """European Index Constituents Query."""


class EuropeanIndexConstituentsData(Data):
    """European Index Constituents data."""

    symbol: str = Field(description="Symbol of the constituent company in the index.")
    price: float = Field(
        description="Current price of the constituent company in the index."
    )
    open: float = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: float = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: float = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float = Field(description=DATA_DESCRIPTIONS.get("volume", ""))

"""ETF Countries data model."""

from typing import List, Set, Union

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class EtfCountriesQueryParams(QueryParams):
    """ETF Countries Query Params."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EtfCountriesData(Data):
    """ETF Countries Data."""

    country: str = Field(description="The country of the exposure.")
    weight: float = Field(description="The weight of the country in the ETF.")

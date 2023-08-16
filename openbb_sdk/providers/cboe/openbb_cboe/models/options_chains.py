"""CBOE Options Chains fetcher."""


from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.options_chains import (
    OptionsChainsData,
    OptionsChainsQueryParams,
)
from pydantic import Field, validator

from openbb_cboe.utils.helpers import get_chains


class CboeOptionsChainsQueryParams(OptionsChainsQueryParams):
    """CBOE Options Chains query.

    Source: https://www.cboe.com/
    """


class CboeOptionsChainsData(OptionsChainsData):
    """CBOE Options Chains Data."""

    contractSymbol: str = Field(
        description="The contract symbol for the option.",
    )
    dte: int = Field(
        description="The days to expiration for the option.",
    )
    bidSize: int = Field(
        description="The bid size for the option.",
    )
    askSize: int = Field(
        description="The ask size for the option.",
    )
    impliedVolatility: float = Field(
        description="The implied volatility of the option.",
    )
    delta: float = Field(
        description="The delta of the option.",
    )
    gamma: float = Field(
        description="The gamma of the option.",
    )
    theta: float = Field(
        description="The theta of the option.",
    )
    rho: float = Field(
        description="The rho of the option.",
    )
    vega: float = Field(
        description="The vega of the option.",
    )
    theoretical: float = Field(
        description="The theoretical value of the option.",
    )
    open: float = Field(
        description="The opening price of the option.",
    )
    high: float = Field(
        description="The high price of the option.",
    )
    low: float = Field(
        description="The low price of the option.",
    )
    lastTradePrice: float = Field(
        description="The last trade price of the option.",
    )
    tick: str = Field(
        description="Whether the last tick was up or down in price.",
    )
    previousClose: float = Field(
        description="The previous closing price of the option.",
    )
    change: float = Field(
        description="The change in  price of the option.",
    )
    changePercent: float = Field(
        description="The change, in percent, of the option.",
    )
    lastTradeTimestamp: datetime = Field(
        description="The last trade timestamp of the option.",
    )

    @validator("expiration", pre=True, check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the datetime object from the date string"""

        return datetime.strptime(v, "%Y-%m-%d")


class CboeOptionsChainsFetcher(
    Fetcher[
        CboeOptionsChainsQueryParams,
        List[CboeOptionsChainsData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints"""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeOptionsChainsQueryParams:
        """Transform the query"""

        return CboeOptionsChainsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CboeOptionsChainsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[CboeOptionsChainsData]:
        """Return the raw data from the CBOE endpoint"""

        return get_chains(query.symbol).to_dict("records")

    @staticmethod
    def transform_data(
        data: List[CboeOptionsChainsData],
    ) -> List[CboeOptionsChainsData]:
        """Transform the data to the standard format"""

        return [CboeOptionsChainsData.parse_obj(d) for d in data]

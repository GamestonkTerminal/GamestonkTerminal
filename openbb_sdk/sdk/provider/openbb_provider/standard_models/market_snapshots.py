"""Market Snapshots  data model."""

from typing import Literal, Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams


class MarketSnapshotsQueryParams(QueryParams):
    """Market Snapshots Query Params"""


class MarketSnapshotsData(Data):
    """Market Snapshots Data"""

    symbol: str = Field(description="The stock symbol.")
    name: str = Field(description="The name associated with the stock symbol.")
    price: Optional[float] = Field(description="The last price of the stock.")
    open: Optional[float] = Field(
        description="The opening price of the stock on the current trading day."
    )
    high: Optional[float] = Field(
        description="The highest price of the stock on the current trading day."
    )
    low: Optional[float] = Field(
        description="The lowest price of the stock on the current trading day."
    )
    prev_close: Optional[float] = Field(
        description="The previous closing price of the stock on the current trading day."
    )
    change: Optional[float] = Field(
        description="The change in price over the current trading day."
    )
    change_percent: Optional[float] = Field(
        description="The change, as a percent, over the current trading day."
    )
    volume: Optional[int] = Field(
        description="The volume of the stock on the current trading day."
    )

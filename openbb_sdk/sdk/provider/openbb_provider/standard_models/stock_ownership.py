"""Stock owner data model."""


from datetime import (
    date as dateType,
    datetime,
)
from typing import Optional

from pydantic import Field, validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.standard_models.base import BaseSymbol
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


def most_recent_quarter(base: dateType = dateType.today()) -> dateType:
    """Get the most recent quarter date.

    Parameter
    ---------
    base : date
        The date to get the most recent quarter.

    Returns
    -------
    date : date
        The most recent quarter date.
    """
    base = min(base, dateType.today())  # This prevents dates from being in the future
    exacts = [(3, 31), (6, 30), (9, 30), (12, 31)]
    for exact in exacts:
        if base.month == exact[0] and base.day == exact[1]:
            return base
    if base.month < 4:
        return dateType(base.year - 1, 12, 31)
    if base.month < 7:
        return dateType(base.year, 3, 31)
    if base.month < 10:
        return dateType(base.year, 6, 30)
    return dateType(base.year, 9, 30)


class StockOwnershipQueryParams(QueryParams, BaseSymbol):
    """Stock ownership Query."""

    date: Optional[dateType] = Field(description=QUERY_DESCRIPTIONS.get("date", ""))
    page: Optional[int] = Field(
        default=0, description="The page number of the data to fetch."
    )

    @validator("date", pre=True, check_fields=False)
    def time_validate(cls, v: str):  # pylint: disable=E021
        """Validate the date."""
        if v is None:
            v = dateType.today()
        if isinstance(v, str):
            base = datetime.strptime(v, "%Y-%m-%d").date()
            return most_recent_quarter(base)
        return most_recent_quarter(v)


class StockOwnershipData(Data):
    """Stock Ownership Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    cik: int = Field(description="The cik of the stock ownership.")
    filing_date: dateType = Field(description="The filing date of the stock ownership.")
    investor_name: str = Field(
        ...,
        description="The investor name of the stock ownership.",
    )
    symbol: str = Field(description="The symbol of the stock ownership.")
    security_name: str = Field(
        ...,
        description="The security name of the stock ownership.",
    )
    type_of_security: str = Field(
        ...,
        description="The type of security of the stock ownership.",
    )
    security_cusip: str = Field(
        ...,
        description="The security cusip of the stock ownership.",
    )
    shares_type: str = Field(description="The shares type of the stock ownership.")
    put_call_share: str = Field(
        ...,
        description="The put call share of the stock ownership.",
    )
    investment_discretion: str = Field(
        ...,
        description="The investment discretion of the stock ownership.",
    )
    industry_title: str = Field(
        ...,
        description="The industry title of the stock ownership.",
    )
    weight: float = Field(description="The weight of the stock ownership.")
    last_weight: float = Field(description="The last weight of the stock ownership.")
    change_in_weight: float = Field(
        ...,
        description="The change in weight of the stock ownership.",
    )
    change_in_weight_percentage: float = Field(
        ...,
        description="The change in weight percentage of the stock ownership.",
    )
    market_value: int = Field(description="The market value of the stock ownership.")
    last_market_value: int = Field(
        ...,
        description="The last market value of the stock ownership.",
    )
    change_in_market_value: int = Field(
        ...,
        description="The change in market value of the stock ownership.",
    )
    change_in_market_value_percentage: float = Field(
        ...,
        description="The change in market value percentage of the stock ownership.",
    )
    shares_number: int = Field(
        ...,
        description="The shares number of the stock ownership.",
    )
    last_shares_number: int = Field(
        ...,
        description="The last shares number of the stock ownership.",
    )
    change_in_shares_number: float = Field(
        ...,
        description="The change in shares number of the stock ownership.",
    )
    change_in_shares_number_percentage: float = Field(
        ...,
        description="The change in shares number percentage of the stock ownership.",
    )
    quarter_end_price: float = Field(
        ...,
        description="The quarter end price of the stock ownership.",
    )
    avg_price_paid: float = Field(
        ...,
        description="The average price paid of the stock ownership.",
    )
    is_new: bool = Field(description="Is the stock ownership new.")
    is_sold_out: bool = Field(description="Is the stock ownership sold out.")
    ownership: float = Field(description="How much is the ownership.")
    last_ownership: float = Field(description="The last ownership amount.")
    change_in_ownership: float = Field(description="The change in ownership amount.")
    change_in_ownership_percentage: float = Field(
        ...,
        description="The change in ownership percentage.",
    )
    holding_period: int = Field(
        ...,
        description="The holding period of the stock ownership.",
    )
    first_added: dateType = Field(
        ...,
        description="The first added date of the stock ownership.",
    )
    performance: float = Field(description="The performance of the stock ownership.")
    performance_percentage: float = Field(
        ...,
        description="The performance percentage of the stock ownership.",
    )
    last_performance: float = Field(
        ...,
        description="The last performance of the stock ownership.",
    )
    change_in_performance: float = Field(
        ...,
        description="The change in performance of the stock ownership.",
    )
    is_counted_for_performance: bool = Field(
        ...,
        description="Is the stock ownership counted for performance.",
    )

"""Price Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/price")

# pylint: disable=unused-argument


@router.command(model="StockQuote")
def quote(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Stock Quote. Load stock data for a specific ticker."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="StockNBBO")
def nbbo(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Stock Quote. Load National Best Bid and Offer for a specific equity."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="StockHistorical")
def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Stock Historical price. Load stock data for a specific ticker."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="PricePerformance")
def performance(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Price performance as a return, over different periods."""
    return OBBject(results=Query(**locals()).execute())

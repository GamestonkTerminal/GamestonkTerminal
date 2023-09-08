### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
import openbb_provider
import pandas
import datetime
import pydantic
from pydantic import validate_arguments, BaseModel
from inspect import Parameter
import typing
from typing import List, Dict, Union, Optional, Literal
from typing_extensions import Annotated
from openbb_core.app.utils import df_to_basemodel
from openbb_core.app.static.filters import filter_inputs

import openbb_core.app.model.command_context
import pydantic.main
import types

class CLASS_stocks_ca(Container):
    """/stocks/ca
peers
    """
    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate_arguments
    def peers(self, symbol: Annotated[Union[str, List[str]], OpenBBCustomParameter(description='Symbol to get data for.')], provider: Optional[Literal['fmp']] = None, **kwargs) -> OBBject[BaseModel]:
        """Company peers.

Parameters
----------
symbol : Union[str, List[str]]
    Symbol to get data for.
provider : Optional[Literal['fmp']]
    The provider to use for the query, by default None.
    If None, the provider specified in defaults is selected or 'fmp' if there is
    no default.

Returns
-------
OBBject
    results : List[StockPeers]
        Serializable results.
    provider : Optional[Literal['fmp']]
        Provider name.
    warnings : Optional[List[Warning_]]
        List of warnings.
    chart : Optional[Chart]
        Chart object.
    metadata: Optional[Metadata]
        Metadata info about the command execution.

StockPeers
----------
symbol : Optional[str]
    Symbol representing the entity requested in the data. 
peers_list : Optional[List[str]]
    A list of stock peers based on sector, exchange and market cap. 
"""  # noqa: E501

        inputs = filter_inputs(
            provider_choices={"provider": provider, },
            standard_params={"symbol": ",".join(symbol) if isinstance(symbol, list) else symbol, },
            extra_params=kwargs,
        )

        return self._command_runner.run(
            "/stocks/ca/peers",
            **inputs,
        )


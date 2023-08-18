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
from typing import List, Dict, Union, Optional, Literal, Annotated
import typing_extensions
from openbb_core.app.utils import df_to_basemodel
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output

import openbb_core.app.model.command_context
import pydantic.main
import types
import typing


class CLASS_fixedincome(Container):
    @filter_call
    @validate_arguments
    def treasury(
        self,
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """Get treasury rates.

        Parameters
        ----------
        start_date : Union[datetime.date, NoneType, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, NoneType, str]
            End date of the data, in YYYY-MM-DD format.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[TreasuryRates]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        TreasuryRates
        -------------
        date : Optional[date]
            The date of the data.
        month_1 : Optional[float]
            1 month treasury rate.
        month_2 : Optional[float]
            2 month treasury rate.
        month_3 : Optional[float]
            3 month treasury rate.
        month_6 : Optional[float]
            6 month treasury rate.
        year_1 : Optional[float]
            1 year treasury rate.
        year_2 : Optional[float]
            2 year treasury rate.
        year_3 : Optional[float]
            3 year treasury rate.
        year_5 : Optional[float]
            5 year treasury rate.
        year_7 : Optional[float]
            7 year treasury rate.
        year_10 : Optional[float]
            10 year treasury rate.
        year_20 : Optional[float]
            20 year treasury rate.
        year_30 : Optional[float]
            30 year treasury rate."""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "start_date": start_date,
                "end_date": end_date,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/fixedincome/treasury",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def ycrv(
        self,
        date: Annotated[
            Optional[datetime.date],
            OpenBBCustomParameter(
                description="Date to get Yield Curve data.  Defaults to the most recent FRED entry."
            ),
        ] = None,
        inflation_adjusted: Annotated[
            Optional[bool],
            OpenBBCustomParameter(description="Get inflation adjusted rates."),
        ] = False,
        chart: bool = False,
        provider: Optional[Literal["fred"]] = None,
        **kwargs
    ) -> OBBject[BaseModel]:
        """Get United States yield curve.

        Parameters
        ----------
        date : Optional[datetime.date]
            Date to get Yield Curve data.  Defaults to the most recent FRED entry.
        inflation_adjusted : Optional[bool]
            Get inflation adjusted rates.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Optional[Literal['fred']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fred' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[USYieldCurve]
                Serializable results.
            provider : Optional[Literal['fred']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        USYieldCurve
        ------------
        maturity : Optional[float]
            Maturity of the treasury rate in years.
        rate : Optional[float]
            Associated rate given in decimal form (0.05 is 5%)"""

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "date": date,
                "inflation_adjusted": inflation_adjusted,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/fixedincome/ycrv",
            **inputs,
        ).output

        return filter_output(o)

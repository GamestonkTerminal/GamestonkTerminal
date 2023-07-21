### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import typing
from typing import Literal, Optional

from pydantic import validate_arguments

import openbb_core.app.model.command_context
import openbb_core.app.model.results.empty
from openbb_core.app.model.command_output import CommandOutput
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output


class CLASS_stocks_ca(Container):
    @filter_call
    @validate_arguments
    def get(
        self,
        symbol: str,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> CommandOutput[typing.List]:
        """Company peers.

        Available providers: fmp,

        Standard
        ========

        Parameter
        ---------
        symbol: str
            The symbol of the company.


        Returns
        -------
        symbol : str
            The symbol of the company to retrieve the stock peers of.
        peers_list : List[str]
            A list of stock peers based on sector, exchange and market cap

        fmp
        ===

        Source: https://site.financialmodelingprep.com/developer/docs/#Stock-Peers

        Parameter
        ---------
        All fields are standardized.
        """
        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": symbol,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/get",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def balance(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company balance sheet."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/balance",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def cashflow(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company cashflow."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/cashflow",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def hcorr(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company historical correlation."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/hcorr",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def hist(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company historical prices."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/hist",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def income(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company income statement."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/income",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def scorr(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company sector correlation."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/scorr",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def screener(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company screener."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/screener",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def sentiment(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company sentiment."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/sentiment",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def similar(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company similar."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/similar",
            **inputs,
        ).output

        return filter_output(o)

    @filter_call
    @validate_arguments
    def volume(
        self, chart: bool = False
    ) -> CommandOutput[openbb_core.app.model.results.empty.Empty]:
        """Company volume."""
        inputs = filter_inputs(
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/ca/volume",
            **inputs,
        ).output

        return filter_output(o)

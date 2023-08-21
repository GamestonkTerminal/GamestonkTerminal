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
from openbb_core.app.static.filters import filter_inputs

import openbb_core.app.model.results.empty


class CLASS_stocks_dps(Container):
    @validate_arguments
    def ctb(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Cost to borrow of stocks."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/ctb",
            **inputs,
        )

    @validate_arguments
    def dpotc(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Dark pools (ATS) vs OTC data."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/dpotc",
            **inputs,
        )

    @validate_arguments
    def ftd(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Fails-to-deliver data."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/ftd",
            **inputs,
        )

    @validate_arguments
    def hsi(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Show top high short interest stocks of over 20% ratio."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/hsi",
            **inputs,
        )

    @validate_arguments
    def pos(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Dark pool short position."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/pos",
            **inputs,
        )

    @validate_arguments
    def prom(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Promising tickers based on dark pool shares regression."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/prom",
            **inputs,
        )

    @validate_arguments
    def psi(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Price vs short interest volume"""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/psi",
            **inputs,
        )

    @validate_arguments
    def psi_q(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/psi_q",
            **inputs,
        )

    @validate_arguments
    def psi_sg(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/psi_sg",
            **inputs,
        )

    @validate_arguments
    def shorted(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Most shorted stocks."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/shorted",
            **inputs,
        )

    @validate_arguments
    def sidtc(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Short interest and days to cover."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/sidtc",
            **inputs,
        )

    @validate_arguments
    def spos(
        self, chart: bool = False
    ) -> OBBject[openbb_core.app.model.results.empty.Empty]:
        """Net short vs position."""

        inputs = filter_inputs(
            chart=chart,
        )

        return self._command_runner.run(
            "/stocks/dps/spos",
            **inputs,
        )

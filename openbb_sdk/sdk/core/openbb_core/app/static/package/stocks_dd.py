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
from openbb_core.app.utils import df_to_basemodel
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output

import openbb_core.app.model.command_context
import types
import typing


class CLASS_stocks_dd(Container):
    @filter_call
    @validate_arguments
    def sec(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        type: Annotated[
            Literal[
                "1",
                "1-A",
                "1-E",
                "1-K",
                "1-N",
                "1-SA",
                "1-U",
                "1-Z",
                "10",
                "10-D",
                "10-K",
                "10-M",
                "10-Q",
                "11-K",
                "12b-25",
                "13F",
                "13H",
                "144",
                "15",
                "15F",
                "17-H",
                "18",
                "18-K",
                "19b-4",
                "19b-4(e)",
                "19b-7",
                "2-E",
                "20-F",
                "24F-2",
                "25",
                "3",
                "4",
                "40-F",
                "5",
                "6-K",
                "7-M",
                "8-A",
                "8-K",
                "8-M",
                "9-M",
                "ABS-15G",
                "ABS-EE",
                "ABS DD-15E",
                "ADV",
                "ADV-E",
                "ADV-H",
                "ADV-NR",
                "ADV-W",
                "ATS",
                "ATS-N",
                "ATS-R",
                "BD",
                "BD-N",
                "BDW",
                "C",
                "CA-1",
                "CB",
                "CFPORTAL",
                "CRS",
                "CUSTODY",
                "D",
                "F-1",
                "F-10",
                "F-3",
                "F-4",
                "F-6",
                "F-7",
                "F-8",
                "F-80",
                "F-N",
                "F-X",
                "ID",
                "MA",
                "MA-I",
                "MA-NR",
                "MA-W",
                "MSD",
                "MSDW",
                "N-14",
                "N-17D-1",
                "N-17f-1",
                "N-17f-2",
                "N-18f-1",
                "N-1A",
                "N-2",
                "N-23c-3",
                "N-27D-1",
                "N-3",
                "N-4",
                "N-5",
                "N-54A",
                "N-54C",
                "N-6",
                "N-6EI-1",
                "N-6F",
                "N-8A",
                "N-8B-2",
                "N-8B-4",
                "N-8F",
                "N-CEN",
            ],
            OpenBBCustomParameter(description="The type of the SEC filing form."),
        ] = "10-K",
        page: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="Page number of the results."),
        ] = 0,
        limit: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 100,
        chart: bool = False,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject[List]:
        """SEC Filings.


        openbb
        ======

        Parameters
        ----------
        provider: Literal[fmp]
            The provider to use for the query.
        symbol : str
            Symbol to get data for.
        type : Literal['1', '1-A', '1-E', '1-K', '1-N', '1-SA', '1-U', '1-Z', '10', '10-D', '10-K', '10-M', '10-Q', '11-K', '12b-25', '13F', '13H', '144', '15', '15F', '17-H', '18', '18-K', '19b-4', '19b-4(e)', '19b-7', '2-E', '20-F', '24F-2', '25', '3', '4', '40-F', '5', '6-K', '7-M', '8-A', '8-K', '8-M', '9-M', 'ABS-15G', 'ABS-EE', 'ABS DD-15E', 'ADV', 'ADV-E', 'ADV-H', 'ADV-NR', 'ADV-W', 'ATS', 'ATS-N', 'ATS-R', 'BD', 'BD-N', 'BDW', 'C', 'CA-1', 'CB', 'CFPORTAL', 'CRS', 'CUSTODY', 'D', 'F-1', 'F-10', 'F-3', 'F-4', 'F-6', 'F-7', 'F-8', 'F-80', 'F-N', 'F-X', 'ID', 'MA', 'MA-I', 'MA-NR', 'MA-W', 'MSD', 'MSDW', 'N-14', 'N-17D-1', 'N-17f-1', 'N-17f-2', 'N-18f-1', 'N-1A', 'N-2', 'N-23c-3', 'N-27D-1', 'N-3', 'N-4', 'N-5', 'N-54A', 'N-54C', 'N-6', 'N-6EI-1', 'N-6F', 'N-8A', 'N-8B-2', 'N-8B-4', 'N-8F', 'N-CEN']
            The type of the SEC filing form.
        page : Optional[int]
            Page number of the results.
        limit : Optional[int]
            The number of data entries to return.

        Returns
        -------
        OBBject
            results: List[Data]
                Serializable results.
            provider: Optional[PROVIDERS]
                Provider name.
            warnings: Optional[List[Warning_]]
                List of warnings.
            error: Optional[Error]
                Caught exceptions.
            chart: Optional[Chart]
                Chart object.


        SECFilings
        ----------
        symbol : str
            Symbol to get data for.
        filling_date : datetime
            The filling date of the SEC filing.
        accepted_date : datetime
            The accepted date of the SEC filing.
        cik : str
            The CIK of the SEC filing.
        type : str
            The type of the SEC filing.
        link : str
            The link of the SEC filing.
        final_link : str
            The final link of the SEC filing.

        fmp
        ===

        Parameters
        ----------
        All fields are standardized.


        SECFilings
        ----------
        All fields are standardized."""  # noqa: E501
        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "type": type,
                "page": page,
                "limit": limit,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/stocks/dd/sec",
            **inputs,
        ).output

        return filter_output(o)

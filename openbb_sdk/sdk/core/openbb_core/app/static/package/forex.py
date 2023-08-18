### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Union

import typing_extensions
from pydantic import validate_arguments

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_call, filter_inputs, filter_output


class CLASS_forex(Container):
    @filter_call
    @validate_arguments
    def load(
        self,
        symbol: typing_extensions.Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        start_date: typing_extensions.Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: typing_extensions.Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        chart: bool = False,
        provider: Union[Literal["fmp", "polygon", "yfinance"], None] = None,
        **kwargs
    ) -> OBBject[List]:
        r"""Forex Intraday Price.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for.
        start_date : Union[datetime.date, NoneType, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, NoneType, str]
            End date of the data, in YYYY-MM-DD format.
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Union[Literal['fmp', 'polygon', 'yfinance'], NoneType]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        timespan : Literal['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']
            The timespan of the data. (provider: polygon)
        sort : Literal['asc', 'desc']
            Sort order of the data. (provider: polygon)
        limit : PositiveInt
            The number of data entries to return. (provider: polygon)
        adjusted : bool
            Whether the data is adjusted. (provider: polygon)
        multiplier : PositiveInt
            The multiplier of the timespan. (provider: polygon)
        interval : Union[Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'], NoneType]
            Data granularity. (provider: yfinance)
        period : Union[Literal['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'], NoneType]
            Period of the data to return. (provider: yfinance)

        Returns
        -------
        OBBject
            results : List[ForexEOD]
                Serializable results.
            provider : Union[Literal['fmp', 'polygon', 'yfinance'], NoneType]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        ForexEOD
        --------
        date : Optional[datetime]
            The date of the data.
        open : Optional[PositiveFloat]
            The open price of the symbol.
        high : Optional[PositiveFloat]
            The high price of the symbol.
        low : Optional[PositiveFloat]
            The low price of the symbol.
        close : Optional[PositiveFloat]
            The close price of the symbol.
        volume : Optional[NonNegativeFloat]
            The volume of the symbol.
        vwap : Optional[PositiveFloat]
            Volume Weighted Average Price of the symbol.
        n : Optional[PositiveInt]
            The number of transactions for the symbol in the time period. (provider: polygon)
        adjClose : Optional[float]
            Adjusted Close Price of the symbol. (provider: fmp)
        unadjustedVolume : Optional[float]
            Unadjusted volume of the symbol. (provider: fmp)
        change : Optional[float]
            Change in the price of the symbol from the previous day. (provider: fmp)
        changePercent : Optional[float]
            Change \% in the price of the symbol. (provider: fmp)
        label : Optional[str]
            Human readable format of the date. (provider: fmp)
        changeOverTime : Optional[float]
            Change \% in the price of the symbol over a period of time. (provider: fmp)
        """

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "start_date": start_date,
                "end_date": end_date,
            },
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/forex/load",
            **inputs,
        )

        return filter_output(o)

    @filter_call
    @validate_arguments
    def pairs(
        self,
        chart: bool = False,
        provider: Union[Literal["fmp", "polygon"], None] = None,
        **kwargs
    ) -> OBBject[List]:
        """Forex Available Pairs.

        Parameters
        ----------
        chart : bool
            Whether to create a chart or not, by default False.
        provider : Union[Literal['fmp', 'polygon'], NoneType]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        symbol : Union[str, NoneType]
            Symbol of the pair to search. (provider: polygon)
        date : Union[datetime.date, NoneType]
            A specific date to get data for. (provider: polygon)
        search : Union[str, NoneType]
            Search for terms within the ticker and/or company name. (provider: polygon)
        active : Union[Literal[True, False], NoneType]
            Specify if the tickers returned should be actively traded on the queried date. (provider: polygon)
        order : Union[Literal['asc', 'desc'], NoneType]
            Order data by ascending or descending. (provider: polygon)
        sort : Union[Literal['ticker', 'name', 'market', 'locale', 'currency_symbol', 'currency_name', 'base_currency_symbol', 'base_currency_name', 'last_updated_utc', 'delisted_utc'], NoneType]
            Sort field used for ordering. (provider: polygon)
        limit : Union[pydantic.types.PositiveInt, NoneType]
            The number of data entries to return. (provider: polygon)

        Returns
        -------
        OBBject
            results : List[ForexPairs]
                Serializable results.
            provider : Union[Literal['fmp', 'polygon'], NoneType]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            error : Optional[Error]
                Caught exceptions.
            chart : Optional[Chart]
                Chart object.

        ForexPairs
        ----------
        name : Optional[str]
            The name of the currency pair.
        market : Optional[str]
            The name of the trading market. Always 'fx'. (provider: polygon)
        locale : Optional[str]
            The locale of the currency pair. (provider: polygon)
        currency_symbol : Optional[str]
            The symbol of the quote currency. (provider: polygon)
        currency_name : Optional[str]
            The name of the quote currency. (provider: polygon)
        base_currency_symbol : Optional[str]
            The symbol of the base currency. (provider: polygon)
        base_currency_name : Optional[str]
            The name of the base currency. (provider: polygon)
        last_updated_utc : Optional[datetime]
            The last updated timestamp in UTC. (provider: polygon)
        delisted_utc : Optional[datetime]
            The delisted timestamp in UTC. (provider: polygon)
        symbol : Optional[str]
            The symbol of the currency pair. (provider: fmp)
        currency : Optional[str]
            The base currency of the currency pair. (provider: fmp)
        stockExchange : Optional[str]
            The stock exchange of the currency pair. (provider: fmp)
        exchange_short_name : Optional[str]
            The short name of the stock exchange of the currency pair. (provider: fmp)
        """

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={},
            extra_params=kwargs,
            chart=chart,
        )

        o = self._command_runner_session.run(
            "/forex/pairs",
            **inputs,
        )

        return filter_output(o)

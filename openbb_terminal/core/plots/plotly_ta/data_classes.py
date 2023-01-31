# pylint: disable=C0302,R0915,R0914,R0913,R0903,R0904

import logging
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import pandas as pd
import pandas_ta as ta

from openbb_terminal.base_helpers import console
from openbb_terminal.common.technical_analysis import ta_helpers
from openbb_terminal.decorators import log_start_end

logger = logging.getLogger(__name__)
datacls_kwargs = {"slots": True} if sys.version_info >= (3, 10) else {}


def columns_regex(df_ta: pd.DataFrame, name: str) -> List[str]:
    """Return columns that match regex name"""
    column_name = df_ta.filter(regex=rf"{name}(?=[^\d]|$)").columns.tolist()

    return column_name


@dataclass(**datacls_kwargs)
class Arguments:
    label: str
    values: Any

    def __post_init__(self):
        if isinstance(self.values, list) and len(self.values) == 1:
            self.values = self.values[0]


@dataclass(**datacls_kwargs)
class TAIndicator:
    name: str
    args: List[Arguments]

    def __post_init__(self):
        self.args = [Arguments(**arg) for arg in self.args]

    def __iter__(self):
        """Return iterator"""
        return iter(self.args)

    def get_args(self, label: str) -> Union[Arguments, None]:
        """Return arguments by label"""
        output = None
        for opt in self.args:
            if opt.label == label:
                output = opt
        return output

    def get_argument_values(self, label: str) -> Union[List[Any], None]:
        """Returns arguments values by label"""
        output = None
        options = self.get_args(label)
        if options is not None:
            output = options.values
        return output


@dataclass(**datacls_kwargs)
class ChartIndicators:
    indicators: Optional[List[TAIndicator]]

    def __post_init__(self):
        self.indicators = (
            [TAIndicator(**indicator) for indicator in self.indicators]
            if self.indicators
            else []
        )

    def get_indicator(self, name: str) -> Union[TAIndicator, None]:
        """Returns indicator with given name"""
        output = None
        for indicator in self.indicators:  # type: ignore
            if indicator.name == name:
                output = indicator
        return output

    def get_indicator_args(self, name: str, label: str) -> Union[Arguments, None]:
        """Returns arguments for given indicator and label"""
        output = None
        indicator = self.get_indicator(name)
        if indicator is not None:
            output = indicator.get_args(label)
        return output

    def get_indicators(self) -> List[TAIndicator]:
        """Return active indicators and their arguments"""
        return self.indicators

    def get_params(self) -> Dict[str, TAIndicator]:
        """Return dictionary of active indicators and their arguments"""
        output = {indicator.name: indicator for indicator in self.indicators}
        return output

    def get_active_ids(self) -> List[str]:
        """Returns list of names of active indicators"""
        active_ids = [indicator.name for indicator in self.indicators]
        return active_ids

    def get_arg_names(self, name: str) -> List[str]:
        """Returns list of argument labels for given indicator"""
        output = []
        indicator = self.get_indicator(name)
        if indicator is not None:
            for opt in indicator.args:
                output.append(opt.label)
        return output

    def get_options_dict(self, name: str) -> Dict[str, Optional[Arguments]]:
        """Returns dictionary of arguments for given indicator"""
        output = None
        options = self.get_arg_names(name)
        if options:
            output = {}
            for opt in options:
                output[opt] = self.get_indicator_args(name, opt)

        return output

    @classmethod
    def from_dict(cls, indicators: Dict[str, Dict[str, Any]]) -> "ChartIndicators":
        """Return ChartIndicators from dictionary"""
        data = []
        for indicator in indicators:
            args = []
            for arg in indicators[indicator]:
                args.append({"label": arg, "values": indicators[indicator][arg]})
            data.append({"name": indicator, "args": args})

        return cls(indicators=data)

    def to_dataframe(
        self, df_ta: pd.DataFrame, ma_mode: List[str] = None
    ) -> pd.DataFrame:
        """Calculate technical analysis indicators and return dataframe"""
        output = df_ta.copy()
        if not output.empty and self.indicators:
            output = TA_Data(output, self, ma_mode).to_dataframe()

        return output

    def get_indicator_data(self, df_ta: pd.DataFrame, indicator: TAIndicator, **kwargs):
        """Return dataframe with technical analysis indicators"""
        output = None
        if self.indicators:
            output = TA_Data(df_ta, self).get_indicator_data(indicator, **kwargs)

        return output


class TA_Data:
    """Process technical analysis data


    Parameters
    ----------
    df_ta : pd.DataFrame
        Dataframe with OHLCV data
    indicators : Union[ChartIndicators, Dict[str, Dict[str, Any]]]
        ChartIndicators object or dictionary with indicators and arguments
        Example:
            dict(
                sma=dict(length=[20, 50, 100]),
                adx=dict(length=14),
                macd=dict(fast=12, slow=26, signal=9),
                rsi=dict(length=14),
            )


    Methods
    -------
    to_dataframe()
        Return dataframe with technical analysis indicators
    get_indicator_data(indicator: TAIndicator, **kwargs)
        Return dataframe given indicator and arguments

    """

    @log_start_end(log=logger)
    def __init__(
        self,
        df_ta: pd.DataFrame,
        indicators: Union[ChartIndicators, Dict[str, Dict[str, Any]]],
        ma_mode: Optional[List[str]] = None,
    ):
        if not isinstance(indicators, ChartIndicators):
            indicators = ChartIndicators.from_dict(indicators)

        self.df_ta = df_ta
        self.indicators = indicators
        self.ma_mode = ma_mode or ["sma", "ema", "wma", "hma", "zlma", "rma"]
        self.close_col = ta_helpers.check_columns(df_ta)
        self.columns = {
            "aroon": ["High", "Low"],
            "adx": ["High", "Low", self.close_col],
            "cci": ["High", "Low", self.close_col],
            "obv": [self.close_col, "Volume"],
            "fisher": ["High", "Low"],
            "kc": ["High", "Low", self.close_col],
            "stoch": ["High", "Low", self.close_col],
            "ad": ["High", "Low", self.close_col, "Volume"],
            "adosc": ["High", "Low", self.close_col, "Volume"],
            "vwap": ["High", "Low", self.close_col, "Volume"],
            "donchian": ["High", "Low"],
        }

    def get_indicator_data(self, indicator: TAIndicator, **args) -> pd.DataFrame:
        """Returns dataframe with indicator data

        Parameters
        ----------
        indicator : TAIndicator
            TAIndicator object
        args : dict
            Arguments for given indicator

        Returns
        -------
        pd.DataFrame
            Dataframe with indicator data
        """
        output = None
        if indicator and indicator.name in self.ma_mode:

            if isinstance(indicator.get_argument_values("length"), list):
                df_ta = pd.DataFrame()

                for length in indicator.get_argument_values("length"):
                    df_ma = getattr(ta, indicator.name)(
                        self.df_ta[self.close_col], length=length
                    )
                    df_ta.insert(0, f"{indicator.name.upper()}_{length}", df_ma)

                output = df_ta

            else:
                output = getattr(ta, indicator.name)(
                    self.df_ta[self.close_col],
                    length=indicator.get_argument_values("length"),
                )
                if indicator.name == "zlma" and output is not None:
                    output.name = output.name.replace("ZL_EMA", "ZLMA")

        elif indicator.name == "vwap":
            ta_columns = self.columns[indicator.name]
            ta_columns = [self.df_ta[col] for col in ta_columns]

            output = getattr(ta, indicator.name)(
                *ta_columns,
            )
        elif indicator.name in self.columns:
            ta_columns = self.columns[indicator.name]
            ta_columns = [self.df_ta[col] for col in ta_columns]

            output = getattr(ta, indicator.name)(*ta_columns, **args)
        else:
            output = getattr(ta, indicator.name)(self.df_ta[self.close_col], **args)

        # Drop NaN values from output and return None if empty
        if output is not None:
            output.dropna(inplace=True)
            if output.empty:
                output = None

        return output

    def to_dataframe(self) -> pd.DataFrame:
        """Returns dataframe with all indicators"""
        active_indicators = self.indicators.get_indicators()

        if not active_indicators:
            return None

        output = self.df_ta
        for indicator in active_indicators:
            if indicator.name in ["fib", "srlines", "clenow", "denmark"]:
                continue
            try:
                indicator_data = self.get_indicator_data(
                    indicator,
                    **self.indicators.get_options_dict(indicator.name)
                    if indicator.name in self.indicators.get_arg_names(indicator.name)
                    else {},
                )
            except Exception as e:
                console.print(
                    f"[red]Error processing indicator {indicator.name}: {e}[/red]"
                )
                indicator_data = None

            if indicator_data is not None:
                output = output.join(indicator_data).interpolate("linear")

        return output

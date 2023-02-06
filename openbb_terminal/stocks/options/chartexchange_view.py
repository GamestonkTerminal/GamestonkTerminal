"""Chartexchange view"""
__docformat__ = "numpy"

import logging
import os
from typing import Union

import pandas as pd

from openbb_terminal.core.plots.plotly_helper import OpenBBFigure
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.rich_config import console
from openbb_terminal.stocks.options import chartexchange_model

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def plot_chart(df: pd.DataFrame, option_type: str, symbol: str) -> OpenBBFigure:
    """Plot Candlestick chart

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with OHLC data
    option_type : str
        Type of option (call or put)
    symbol : str
        Ticker symbol

    Returns
    -------
    OpenBBFigure
        Plotly figure object
    """

    fig = OpenBBFigure.create_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        row_width=[0.2, 0.7],
        subplot_titles=["", "Volume"],
    )
    fig.set_title(f"Historical {symbol} {option_type}")

    fig.add_candlestick(
        open=df.Open,
        high=df.High,
        low=df.Low,
        close=df.Close,
        x=df.index,
        name=f"OHLC {symbol}",
        row=1,
        col=1,
    )
    fig.add_stock_volume(df)
    fig.hide_holidays()

    return fig


@log_start_end(log=logger)
def display_raw(
    symbol: str = "GME",
    expiry: str = "2021-02-05",
    call: bool = True,
    price: float = 90,
    limit: int = 10,
    export: str = "",
    sheet_name: str = None,
    external_axes: bool = False,
) -> Union[OpenBBFigure, None]:
    """Return raw stock data[chartexchange]

    Parameters
    ----------
    symbol : str
        Ticker symbol for the given option
    expiry : str
        The expiry of expiration, format "YYYY-MM-DD", i.e. 2010-12-31.
    call : bool
        Whether the underlying asset should be a call or a put
    price : float
        The strike of the expiration
    limit : int
        Number of rows to show
    export : str
        Export data as CSV, JSON, XLSX
    external_axes: Optional[List[plt.Axes]]
        External axes (1 axis is expected in the list), by default None
    """

    df = chartexchange_model.get_option_history(symbol, expiry, call, price)[::-1]
    if df.empty:
        return console.print("[red]No data found[/red]\n")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")

    option_type = "call" if call else "put"

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "hist",
        df,
        sheet_name,
    )
    print_rich_table(
        df.head(limit),
        headers=list(df.columns),
        show_index=True,
        title=f"{symbol.upper()} raw data",
    )

    fig = plot_chart(df, option_type, symbol)

    return fig.show(external=external_axes)

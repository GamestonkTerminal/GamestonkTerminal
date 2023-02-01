"""Tradier options view"""
__docformat__ = "numpy"

import logging
import os
import warnings

from openbb_terminal.core.plots.plotly_helper import OpenBBFigure
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.stocks.options import tradier_model

logger = logging.getLogger(__name__)

warnings.filterwarnings("ignore")


# pylint: disable=too-many-arguments
@log_start_end(log=logger)
def display_historical(
    symbol: str,
    expiry: str,
    strike: float = 0,
    put: bool = False,
    raw: bool = False,
    chain_id: str = None,
    export: str = "",
    sheet_name: str = "",
    external_axes: bool = False,
):
    """Plot historical option prices

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    expiry: str
        Expiry date of option
    strike: float
        Option strike price
    put: bool
        Is this a put option?
    raw: bool
        Print raw data
    chain_id: str
        OCC option symbol
    export: str
        Format of export file
    sheet_name: str
        Optionally specify the name of the sheet to export to
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """

    df_hist = tradier_model.get_historical_options(
        symbol, expiry, strike, put, chain_id
    )

    if raw:
        print_rich_table(
            df_hist,
            headers=[x.title() for x in df_hist.columns],
            title="Historical Option Prices",
        )

    op_type = ["call", "put"][put]

    if export:
        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "hist",
            df_hist,
            sheet_name,
        )

    fig = OpenBBFigure.create_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02,
        row_heights=[0.3, 0.7],
        subplot_titles=[f"{symbol} {strike} {op_type}", "Volume"],
    )
    fig.set_title(f"Historical {strike} {op_type.title()}")

    fig.add_candlestick(
        open=df_hist["Open"],
        high=df_hist["High"],
        low=df_hist["Low"],
        close=df_hist["Close"],
        x=df_hist.index,
        name=f"{symbol} OHLC",
        row=1,
        col=1,
    )
    fig.add_volume(
        y=df_hist["Volume"],
        x=df_hist.index,
        name="Volume",
        row=2,
        col=1,
    )
    fig.hide_holidays()

    return fig.show(external=external_axes)

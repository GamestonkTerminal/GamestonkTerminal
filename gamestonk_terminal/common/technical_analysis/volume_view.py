"""Volume View"""
__docformat__ = "numpy"

import os
from datetime import timedelta

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.common.technical_analysis import volume_model
from gamestonk_terminal.config_plot import PLOT_DPI
from gamestonk_terminal.helper_funcs import export_data, plot_autoscale

register_matplotlib_converters()


def plot_ad(
    s_ticker: str, s_interval: str, df_stock: pd.DataFrame, use_open: bool, export: str
):
    """Plot AD tecnhical inticator

    Parameters
    ----------
    s_ticker : str
        Ticker
    s_interval : str
        Interval of data
    df_stock : pd.DataFrame
        Dataframe of prices
    use_open : bool
        Whether to use open prices in calculation
    export: str
        Format to export data as
    """
    df_ta = volume_model.ad(df_stock, use_open)
    if export:
        export_data(export, os.path.dirname(os.path.abspath(__file__)), "ad", df_ta)

    bar_colors = ["r" if x[1].Open < x[1].Close else "g" for x in df_stock.iterrows()]

    if s_interval == "1440min":
        bar_width = timedelta(days=1)
    else:
        bar_width = timedelta(minutes=int(s_interval.split("m")[0]))

    fig, axes = plt.subplots(
        3,
        1,
        gridspec_kw={"height_ratios": [2, 1, 1]},
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    ax = axes[0]
    if s_interval == "1440min":
        ax.plot(df_stock.index, df_stock["Adj Close"].values, "k", lw=2)
    else:
        ax.plot(df_stock.index, df_stock["Close"].values, "k", lw=2)
    ax.set_title(f"{s_ticker} AD")
    ax.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax.set_ylabel("Share Price ($)")
    ax.grid(b=True, which="major", color="#666666", linestyle="-")

    ax2 = axes[1]
    ax2.set_ylabel("Volume")
    if s_interval == "1440min":
        ax2.bar(
            df_stock.index,
            df_stock["Volume"].values,
            color=bar_colors,
            alpha=0.8,
            width=0.3,
        )
    else:
        ax2.bar(
            df_stock.index,
            df_stock["Volume"].values,
            color=bar_colors,
            alpha=0.8,
            width=bar_width,
        )
    ax2.set_xlim(df_stock.index[0], df_stock.index[-1])

    ax3 = axes[2]
    ax3.plot(df_ta.index, df_ta.values, "b", lw=1)
    ax3.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax3.axhline(0, linewidth=2, color="k", ls="--")
    ax3.set_ylabel("A/D")
    ax3.set_xlabel("Time")
    ax3.grid(b=True, which="major", color="#666666", linestyle="-")

    if gtff.USE_ION:
        plt.ion()

    plt.gcf().autofmt_xdate()
    fig.tight_layout(pad=1)

    plt.show()
    print("")


def plot_obv(s_ticker: str, s_interval: str, df_stock: pd.DataFrame, export: str):
    """Plot OBV tecnhical inticator

    Parameters
    ----------
    s_ticker : str
        Ticker
    s_interval : str
        Interval of data
    df_stock : pd.DataFrame
        Dataframe of prices
    export: str
        Format to export data as
    """
    df_ta = volume_model.obv(s_interval, df_stock)
    if export:
        export_data(export, os.path.dirname(os.path.abspath(__file__)), "obv", df_ta)

    bar_colors = ["r" if x[1].Open < x[1].Close else "g" for x in df_stock.iterrows()]

    if s_interval == "1440min":
        bar_width = timedelta(days=1)
    else:
        bar_width = timedelta(minutes=int(s_interval.split("m")[0]))
    fig, axes = plt.subplots(
        3,
        1,
        gridspec_kw={"height_ratios": [2, 1, 1]},
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    ax = axes[0]
    if s_interval == "1440min":
        ax.plot(df_stock.index, df_stock["Adj Close"].values, "k", lw=2)
    else:
        ax.plot(df_stock.index, df_stock["Close"].values, "k", lw=2)

    ax.set_title(f"{s_ticker} OBV")
    ax.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax.set_ylabel("Share Price ($)")
    ax.grid(b=True, which="major", color="#666666", linestyle="-")
    ax.minorticks_on()
    ax.grid(b=True, which="minor", color="#999999", linestyle="-", alpha=0.2)
    ax2 = axes[1]
    ax2.set_xlim(df_stock.index[0], df_stock.index[-1])

    if s_interval == "1440min":
        ax2.bar(
            df_stock.index,
            df_stock["Volume"].values,
            color=bar_colors,
            alpha=0.8,
            width=bar_width,
        )
    else:
        ax2.bar(
            df_stock.index,
            df_stock["Volume"].values,
            color=bar_colors,
            alpha=0.8,
            width=bar_width,
        )
    ax3 = axes[2]
    ax3.plot(df_ta.index, df_ta.values, "b", lw=1)
    ax3.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax3.set_xlabel("Time")
    ax3.grid(b=True, which="major", color="#666666", linestyle="-")
    ax3.minorticks_on()
    ax3.grid(b=True, which="minor", color="#999999", linestyle="-", alpha=0.2)

    if gtff.USE_ION:
        plt.ion()

    plt.gcf().autofmt_xdate()
    fig.tight_layout(pad=1)

    plt.show()
    print("")

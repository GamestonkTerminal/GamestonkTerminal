"""Quantitative Analysis View"""
__docformat__ = "numpy"

# pylint: disable=too-many-lines


import logging
import os
import traceback
import warnings
from datetime import datetime
from typing import Any, List, Optional

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from detecta import detect_cusum
from pandas.plotting import register_matplotlib_converters
from scipy import stats
from statsmodels.graphics.gofplots import qqplot

from openbb_terminal.common.quantitative_analysis import qa_model
from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal.config_terminal import theme
from openbb_terminal.core.plots.plotly_helper import OpenBBFigure
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    lambda_long_number_format,
    plot_autoscale,
    print_rich_table,
    reindex_dates,
)
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)

register_matplotlib_converters()


def lambda_color_red(val: Any) -> str:
    """Adds red to dataframe value"""
    if val > 0.05:
        return f"[red]{round(val,4)}[/red]"
    return round(val, 4)


@log_start_end(log=logger)
def display_summary(data: pd.DataFrame, export: str = "") -> None:
    """Prints table showing summary statistics

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame to get statistics of
    export : str
        Format to export data
    """
    summary = qa_model.get_summary(data)

    print_rich_table(
        summary,
        headers=list(summary.columns),
        floatfmt=".3f",
        show_index=True,
        title="[bold]Summary Statistics[/bold]",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "summary",
        summary,
    )


@log_start_end(log=logger)
def display_hist(
    data: pd.DataFrame,
    target: str,
    symbol: str = "",
    bins: int = 15,
    external_axes: bool = False,
) -> None:
    """Plots histogram of data

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe to look at
    target : str
        Data column to get histogram of the dataframe
    symbol : str
        Name of dataset
    bins : int
        Number of bins in histogram
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.hist(data=df, target="Adj Close")
    """
    data = data[target]

    fig = OpenBBFigure.create_subplots(1, 1, specs=[[{"secondary_y": True}]])

    if isinstance(data.index[0], datetime):
        start = data.index[0]
        fig.set_title(
            f"Histogram of {symbol} {target} from {start.strftime('%Y-%m-%d')}"
        )
    else:
        fig.set_title(f"Histogram of {symbol} {target}")

    fig.add_histplot(
        data,
        name="Univariate distribution",
        colors=[theme.up_color],
        bins=bins,
        secondary_y=True,
    )
    fig.add_box(
        x=data,
        y=[0.002] * len(data),
        name="Marginal distributions",
        boxmean=True,
        boxpoints="all",
        marker=dict(
            color=theme.down_color,
            symbol="line-ns-open",
        ),
        jitter=0.3,
        hoveron="points",
        secondary_y=True,
    )

    fig.update_layout(
        xaxis_title="Value",
        yaxis2_title="Proportion",
        bargap=0.01,
        bargroupgap=0,
    )
    fig.update_traces(
        selector=dict(type="histogram"),
        marker=dict(
            color=theme.up_color,
            line=dict(color="white", width=2.5),
        ),
    )

    max_y = 0
    for trace in fig.select_traces(selector=dict(type="scatter")):
        if trace.yaxis == "y2" and not isinstance(trace.y[0], str):
            max_y = max(max_y, max(trace.y)) * 1.3

    fig.update_yaxes(range=[0, max_y], secondary_y=True)

    return fig.show() if not external_axes else fig


@log_start_end(log=logger)
def display_cdf(
    data: pd.DataFrame,
    target: str,
    symbol: str = "",
    export: str = "",
    external_axes: list = None,
):
    """Plots Cumulative Distribution Function

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe to look at
    target : str
        Data column
    symbol : str
        Name of dataset
    export : str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.cdf(data=df, target="Adj Close")
    """
    data = data[target]
    start = data.index[0]
    cdf = data.value_counts().sort_index().div(len(data)).cumsum()

    minVal = data.values.min()
    q25 = np.quantile(data.values, 0.25)
    medianVal = np.quantile(data.values, 0.5)
    q75 = np.quantile(data.values, 0.75)
    labels = [
        (minVal, q25),
        (0.25, 0.25),
        "Q1",
        (q25, q25),
        (0, 0.25),
        "Q1",
        (minVal, medianVal),
        (0.5, 0.5),
        "Median",
        (medianVal, medianVal),
        (0, 0.5),
        "Median",
        (minVal, q75),
        (0.75, 0.75),
        "Q3",
        (q75, q75),
        (0, 0.75),
        "Q3",
    ]

    fig = OpenBBFigure()

    fig.add_scatter(
        x=cdf.index,
        y=cdf.values,
        name="Cumulative Distribution Function",
        marker_color=theme.up_color,
        mode="lines",
    )

    for xt, yt, label in zip(labels[::3], labels[1::3], labels[2::3]):
        fig.add_annotation(
            x=minVal + (xt[1] - minVal) / 2,
            y=yt[1] + 0.04,
            text=label,
            showarrow=False,
            font=dict(color=theme.down_color),
        )
        fig.add_shape(
            type="line",
            x0=xt[0],
            y0=yt[0],
            x1=xt[1],
            y1=yt[1],
            line=dict(color=theme.down_color, width=1.5, dash="dash"),
        )

    fig.update_layout(
        title=f"Cumulative Distribution Function of {symbol} {target} from {start.strftime('%Y-%m-%d')}",
        xaxis_title=target.title(),
        yaxis_title="Probability",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "cdf",
        pd.DataFrame(cdf),
    )

    return fig.show() if not external_axes else fig


@log_start_end(log=logger)
def display_bw(
    data: pd.DataFrame,
    target: str,
    symbol: str = "",
    yearly: bool = True,
    external_axes: bool = False,
) -> None:
    """Plots box and whisker plots

    Parameters
    ----------
    symbol : str
        Name of dataset
    data : pd.DataFrame
        Dataframe to look at
    target : str
        Data column to look at
    yearly : bool
        Flag to indicate yearly accumulation
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.bw(data=df, target="Adj Close")
    """
    start = data[target].index[0]

    color = theme.get_colors()[0]
    x_data = data[target].index.year if yearly else data[target].index.month

    l_months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    fig = OpenBBFigure(
        title=f"{['Monthly','Yearly'][yearly]} box plot of {symbol} {target} from {start.strftime('%Y-%m-%d')}",
        yaxis_title=target,
        xaxis_title=["Monthly", "Yearly"][yearly],
    )

    data["x_data"] = x_data

    for i, group in enumerate(data["x_data"].unique()):
        x = group if yearly else l_months[group - 1]
        y = data[data["x_data"] == group][target]
        fig.add_box(
            y=y,
            x=[x] * len(y),
            name=str(x),
            marker=dict(
                color=theme.up_color,
                outliercolor=theme.up_color,
            ),
            fillcolor=theme.get_colors()[i],
            line_color=color,
            boxmean=True,
            whiskerwidth=1,
            boxpoints="suspectedoutliers",
            hoveron="points",
            showlegend=False,
        )

        fig.add_shape(
            type="line",
            x0=x,
            y0=y.min(),
            x1=x,
            y1=y.max(),
            line=dict(color=color, width=1.5, dash="dash"),
        )

    return fig.show() if not external_axes else fig


def create_corr_plot(
    fig: OpenBBFigure,
    series: pd.DataFrame,
    lags: int = 15,
    row: int = 1,
    col: int = 1,
    pacf: bool = False,
):
    corr_array = (
        sm.tsa.stattools.pacf(np.diff(np.diff(series.values)), nlags=lags, method="ywm")
        if pacf
        else sm.tsa.stattools.acf(np.diff(np.diff(series.values)), nlags=lags)
    )
    try:
        lower_y = np.array(
            [
                sm.tsa.stattools.acf(
                    np.diff(np.diff(series.values)), nlags=lags, alpha=0.05
                )[0][x]
                for x in range(lags + 1)
            ]
        )
        upper_y = np.array(
            [
                sm.tsa.stattools.acf(
                    np.diff(np.diff(series.values)), nlags=lags, alpha=0.05
                )[0][x]
                for x in range(lags + 1)
            ]
        )

        for x in range(lags + 1):
            fig.add_scatter(
                x=(x, x),
                y=(0, corr_array[x]),
                mode="lines",
                line_color="white",
                row=row,
                col=col,
            )

        fig.add_scatter(
            x=np.arange(lags + 1),
            y=upper_y,
            mode="lines",
            line_color="rgba(255,255,255,0)",
        )
        fig.add_scatter(
            x=np.arange(lags + 1),
            y=lower_y,
            mode="lines",
            fillcolor="rgba(32, 146, 230,0.3)",
            fill="tonexty",
            line_color="rgba(255,255,255,0)",
        )
        fig.update_traces(showlegend=False)
        fig.update_yaxes(zerolinecolor="white")
    except Exception:
        traceback.print_exc()

    return fig


@log_start_end(log=logger)
def display_acf(
    data: pd.DataFrame,
    target: str,
    symbol: str = "",
    lags: int = 15,
    external_axes: bool = False,
) -> None:
    """Plots Auto and Partial Auto Correlation of returns and change in returns

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe to look at
    target : str
        Data column to look at
    symbol : str
        Name of dataset
    lags : int
        Max number of lags to look at
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.acf(data=df, target="Adj Close")
    """
    data = data[target]
    start = data.index[0]

    # This plot has 4 axes
    fig, axes = plt.subplots(
        nrows=2,
        ncols=2,
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    (ax1, ax2), (ax3, ax4) = axes

    # Diff Auto - correlation function for original time series
    sm.graphics.tsa.plot_acf(np.diff(np.diff(data.values)), lags=lags, ax=ax1)
    ax1.set_title(f"{symbol} Returns Auto-Correlation", fontsize=9)
    # Diff Partial auto - correlation function for original time series
    sm.graphics.tsa.plot_pacf(
        np.diff(np.diff(data.values)), lags=lags, ax=ax2, method="ywm"
    )
    ax2.set_title(
        f"{symbol} Returns Partial Auto-Correlation",
        fontsize=9,
    )

    # Diff Diff Auto-correlation function for original time series
    sm.graphics.tsa.plot_acf(np.diff(np.diff(data.values)), lags=lags, ax=ax3)
    ax3.set_title(
        f"Change in {symbol} Returns Auto-Correlation",
        fontsize=9,
    )
    # Diff Diff Partial auto-correlation function for original time series
    sm.graphics.tsa.plot_pacf(
        np.diff(np.diff(data.values)), lags=lags, ax=ax4, method="ywm"
    )
    ax4.set_title(
        f"Change in {symbol} Returns Partial Auto-Correlation",
        fontsize=9,
    )

    fig.suptitle(
        f"ACF differentials starting from {start.strftime('%Y-%m-%d')}",
        fontsize=15,
        x=0.042,
        y=0.95,
        horizontalalignment="left",
        verticalalignment="top",
    )
    theme.style_primary_axis(ax1)
    theme.style_primary_axis(ax2)
    theme.style_primary_axis(ax3)
    theme.style_primary_axis(ax4)

    if external_axes is None:
        theme.visualize_output(force_tight_layout=True)

    fig = OpenBBFigure.create_subplots(
        rows=2,
        cols=2,
        subplot_titles=[
            f"{symbol} Returns Auto-Correlation",
            f"{symbol} Returns Partial Auto-Correlation",
            f"Change in {symbol} Returns Auto-Correlation",
            f"Change in {symbol} Returns Partial Auto-Correlation",
        ],
        shared_xaxes=True,
        shared_yaxes=True,
        vertical_spacing=0.1,
        horizontal_spacing=0.1,
        x_title="Lag",
        y_title="Correlation",
    ).set_title(title=f"ACF differentials starting from {start.strftime('%Y-%m-%d')}")

    fig = create_corr_plot(
        fig=fig,
        series=data,
        lags=lags,
        row=1,
        col=1,
        pacf=False,
    )
    fig = create_corr_plot(
        fig=fig,
        series=data,
        lags=lags,
        row=1,
        col=2,
        pacf=True,
    )
    fig = create_corr_plot(
        fig=fig,
        series=data,
        lags=lags,
        row=2,
        col=1,
        pacf=False,
    )
    fig = create_corr_plot(
        fig=fig,
        series=data,
        lags=lags,
        row=2,
        col=2,
        pacf=True,
    )

    fig.show()


@log_start_end(log=logger)
def display_qqplot(
    data: pd.DataFrame,
    target: str,
    symbol: str = "",
    external_axes: bool = False,
) -> None:
    """Plots QQ plot for data against normal quantiles

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe
    target : str
        Column in data to look at
    symbol : str
        Stock ticker
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.qqplot(data=df, target="Adj Close")
    """
    # Statsmodels has a UserWarning for marker kwarg-- which we don't use
    warnings.filterwarnings(category=UserWarning, action="ignore")
    data = data[target]

    # This plot has 1 axis
    _, ax = plt.subplots(
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )

    qqplot(
        data,
        stats.distributions.norm,
        fit=True,
        line="45",
        color=theme.down_color,
        ax=ax,
    )
    ax.get_lines()[1].set_color(theme.up_color)

    ax.set_title(f"Q-Q plot for {symbol} {target}")
    ax.set_ylabel("Sample quantiles")
    ax.set_xlabel("Theoretical quantiles")

    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()


@log_start_end(log=logger)
def display_cusum(
    data: pd.DataFrame,
    target: str,
    threshold: float = 5,
    drift: float = 2.1,
    external_axes: bool = False,
):
    """Plots Cumulative sum algorithm (CUSUM) to detect abrupt changes in data

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe
    target : str
        Column of data to look at
    threshold : float
        Threshold value
    drift : float
        Drift parameter
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.cusum(data=df, target="Adj Close")
    """
    target_series = data[target].values

    # The code for this plot was adapted from detecta's sources because at the
    # time of writing this detect_cusum had a bug related to external axes support.
    # see https:  // github.com/demotu/detecta/pull/3
    tap, tan = 0, 0
    ta, tai, taf, _ = detect_cusum(
        x=target_series,
        threshold=threshold,
        drift=drift,
        ending=True,
        show=False,
    )
    # Thus some variable names are left unchanged and unreadable...
    gp, gn = np.zeros(target_series.size), np.zeros(target_series.size)
    for i in range(1, target_series.size):
        s = target_series[i] - target_series[i - 1]
        gp[i] = gp[i - 1] + s - drift  # cumulative sum for + change
        gn[i] = gn[i - 1] - s - drift  # cumulative sum for - change
        if gp[i] < 0:
            gp[i], tap = 0, i
        if gn[i] < 0:
            gn[i], tan = 0, i
        if gp[i] > threshold or gn[i] > threshold:  # change detected!
            ta = np.append(ta, i)  # alarm index
            tai = np.append(tai, tap if gp[i] > threshold else tan)  # start
            gp[i], gn[i] = 0, 0  # reset alarm

    _, axes = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    (ax1, ax2) = axes

    target_series_indexes = range(data[target].size)
    ax1.plot(target_series_indexes, target_series)
    if len(ta):
        ax1.plot(
            tai,
            target_series[tai],
            ">",
            markerfacecolor=theme.up_color,
            markersize=5,
            label="Start",
        )
        ax1.plot(
            taf,
            target_series[taf],
            "<",
            markerfacecolor=theme.down_color,
            markersize=5,
            label="Ending",
        )
        ax1.plot(
            ta,
            target_series[ta],
            "o",
            markerfacecolor=theme.get_colors()[-1],
            markeredgecolor=theme.get_colors()[-2],
            markeredgewidth=1,
            markersize=3,
            label="Alarm",
        )
        ax1.legend()
    ax1.set_xlim(-0.01 * target_series.size, target_series.size * 1.01 - 1)
    ax1.set_ylabel("Amplitude")
    ymin, ymax = (
        target_series[np.isfinite(target_series)].min(),
        target_series[np.isfinite(target_series)].max(),
    )
    y_range = ymax - ymin if ymax > ymin else 1
    ax1.set_ylim(ymin - 0.1 * y_range, ymax + 0.1 * y_range)
    ax1.set_title(
        "Time series and detected changes "
        + f"(threshold= {threshold:.3g}, drift= {drift:.3g}): N changes = {len(tai)}",
        fontsize=10,
    )
    theme.style_primary_axis(ax1)

    ax2.plot(target_series_indexes, gp, label="+")
    ax2.plot(target_series_indexes, gn, label="-")
    ax2.set_xlim(-0.01 * target_series.size, target_series.size * 1.01 - 1)
    ax2.set_xlabel("Data points")
    ax2.set_ylim(-0.01 * threshold, 1.1 * threshold)
    ax2.axhline(threshold)
    theme.style_primary_axis(ax2)

    ax2.set_title(
        "Time series of the cumulative sums of positive and negative changes",
        fontsize=10,
    )
    ax2.legend()

    if external_axes is None:
        theme.visualize_output()


@log_start_end(log=logger)
def display_seasonal(
    symbol: str,
    data: pd.DataFrame,
    target: str,
    multiplicative: bool = False,
    export: str = "",
    external_axes: bool = False,
) -> None:
    """Plots seasonal decomposition data

    Parameters
    ----------
    symbol : str
        Name of dataset
    data : pd.DataFrame
        DataFrame
    target : str
        Column of data to look at
    multiplicative : bool
        Boolean to indicate multiplication instead of addition
    export : str
        Format to export trend and cycle data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    data = data[target]
    result, cycle, trend = qa_model.get_seasonal_decomposition(data, multiplicative)

    plot_data = pd.merge(
        data,
        result.trend,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_result.trend"),
    )
    plot_data = pd.merge(
        plot_data,
        result.seasonal,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_result.seasonal"),
    )
    plot_data = pd.merge(
        plot_data,
        result.resid,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_result.resid"),
    )
    plot_data = pd.merge(
        plot_data,
        cycle,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_cycle"),
    )
    plot_data = pd.merge(
        plot_data,
        trend,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_trend"),
    )
    plot_data = reindex_dates(plot_data)

    # This plot has 1 axis
    fig, axes = plt.subplots(
        4,
        1,
        sharex=True,
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    (ax1, ax2, ax3, ax4) = axes

    colors = iter(theme.get_colors())

    ax1.set_title(f"{symbol} (Time-Series) {target} seasonal decomposition")
    ax1.plot(
        plot_data.index, plot_data[target].values, color=next(colors), label="Values"
    )
    ax1.set_xlim([plot_data.index[0], plot_data.index[-1]])
    ax1.legend()

    # Multiplicative model
    ax2.plot(plot_data["trend"], color=theme.down_color, label="Cyclic-Trend")
    ax2.plot(
        plot_data["trend_cycle"],
        color=theme.up_color,
        linestyle="--",
        label="Cycle component",
    )
    ax2.legend()

    ax3.plot(plot_data["trend_trend"], color=next(colors), label="Trend component")
    ax3.plot(plot_data["seasonal"], color=next(colors), label="Seasonal effect")
    ax3.legend()

    ax4.plot(plot_data["resid"], color=next(colors), label="Residuals")
    ax4.legend()

    theme.style_primary_axis(ax1)
    theme.style_primary_axis(ax2)
    theme.style_primary_axis(ax3)
    theme.style_primary_axis(
        ax4,
        data_index=plot_data.index.to_list(),
        tick_labels=plot_data["date"].to_list(),
    )

    if external_axes is None:
        fig.tight_layout(pad=theme.tight_layout_padding)
        fig.subplots_adjust(
            hspace=0.1,
        )
        theme.visualize_output(force_tight_layout=False)

    # From #https:  // otexts.com/fpp2/seasonal-strength.html
    console.print("Time-Series Level is " + str(round(data.mean(), 2)))

    Ft = max(0, 1 - np.var(result.resid)) / np.var(result.trend + result.resid)
    console.print(f"Strength of Trend: {Ft:.4f}")

    Fs = max(
        0,
        1 - np.var(result.resid) / np.var(result.seasonal + result.resid),
    )
    console.print(f"Strength of Seasonality: {Fs:.4f}\n")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "summary",
        cycle.join(trend),
    )


@log_start_end(log=logger)
def display_normality(data: pd.DataFrame, target: str, export: str = "") -> None:
    """Prints table showing normality statistics

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame
    target : str
        Column in data to look at
    export : str
        Format to export data
    """
    data = data[target]
    normal = qa_model.get_normality(data)
    stats1 = normal.copy().T
    stats1.iloc[:, 1] = stats1.iloc[:, 1].apply(lambda x: lambda_color_red(x))

    print_rich_table(
        stats1,
        show_index=True,
        headers=["Statistic", "p-value"],
        floatfmt=".4f",
        title="[bold]Normality Statistics[/bold]",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "normality",
        normal,
    )


@log_start_end(log=logger)
def display_unitroot(
    data: pd.DataFrame,
    target: str,
    fuller_reg: str = "c",
    kpss_reg: str = "c",
    export: str = "",
):
    """Prints table showing unit root test calculations

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame
    target : str
        Column of data to look at
    fuller_reg : str
        Type of regression of ADF test. Can be ‘c’,’ct’,’ctt’,’nc’ 'c' - Constant and t - trend order
    kpss_reg : str
        Type of regression for KPSS test. Can be ‘c’,’ct'
    export : str
        Format for exporting data
    """
    data = data[target]
    data = qa_model.get_unitroot(data, fuller_reg, kpss_reg)
    print_rich_table(
        data,
        show_index=True,
        headers=list(data.columns),
        title="[bold]Unit Root Calculation[/bold]",
        floatfmt=".4f",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "unitroot",
        data,
    )


@log_start_end(log=logger)
def display_raw(
    data: pd.DataFrame,
    sortby: str = "",
    ascend: bool = False,
    limit: int = 20,
    export: str = "",
) -> None:
    """Prints table showing raw stock data

    Parameters
    ----------
    data : DataFrame
        DataFrame with historical information
    sortby : str
        The column to sort by
    ascend : bool
        Whether to sort descending
    limit : int
        Number of rows to show
    export : str
        Export data as CSV, JSON, XLSX
    """

    if isinstance(data, pd.Series):
        df1 = pd.DataFrame(data)
    else:
        df1 = data.copy()

    if sortby:
        try:
            sort_col = [x.lower().replace(" ", "") for x in df1.columns].index(
                sortby.lower().replace(" ", "")
            )
        except ValueError:
            console.print("[red]The provided column is not a valid option[/red]\n")
            return
        df1 = df1.sort_values(by=data.columns[sort_col], ascending=ascend)
    else:
        df1 = df1.sort_index(ascending=ascend)
    df1.index = [x.strftime("%Y-%m-%d") for x in df1.index]

    print_rich_table(
        df1.head(limit),
        headers=[x.title() if x != "" else "Date" for x in df1.columns],
        title="[bold]Raw Data[/bold]",
        show_index=True,
        floatfmt=".3f",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "raw",
        data,
    )


@log_start_end(log=logger)
def display_line(
    data: pd.Series,
    title: str = "",
    log_y: bool = True,
    markers_lines: Optional[List[datetime]] = None,
    markers_scatter: Optional[List[datetime]] = None,
    export: str = "",
    external_axes: bool = False,
) -> None:
    """Display line plot of data

    Parameters
    ----------
    data: pd.Series
        Data to plot
    title: str
        Title for plot
    log_y: bool
        Flag for showing y on log scale
    markers_lines: Optional[List[datetime]]
        List of dates to highlight using vertical lines
    markers_scatter: Optional[List[datetime]]
        List of dates to highlight using scatter
    export: str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.qa.line(data=df["Adj Close"])
    """
    # This plot has 1 axis
    _, ax = plt.subplots(
        figsize=plot_autoscale(),
        dpi=PLOT_DPI,
    )
    fig = OpenBBFigure()

    if log_y:
        ax.semilogy(data.index, data.values)
        ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax.yaxis.set_major_locator(
            matplotlib.ticker.LogLocator(base=100, subs=[1.0, 2.0, 5.0, 10.0])
        )
        ax.ticklabel_format(style="plain", axis="y")
        fig.add_scatter(
            x=data.index,
            y=data.values,
            name="",
            mode="lines",
            showlegend=False,
        )
        fig.update_layout(xaxis_type="log")

    else:
        ax.plot(data.index, data.values)
        fig.add_scatter(
            x=data.index,
            y=data.values,
            name="",
            mode="lines",
            showlegend=False,
        )

        if markers_lines:
            ymin, ymax = ax.get_ylim()
            ax.vlines(markers_lines, ymin, ymax, color="#00AAFF")
            fig.add_shape(
                type="line",
                x0=markers_lines,
                y0=ymin,
                x1=markers_lines,
                y1=ymax,
                line=dict(color="#00AAFF", width=2),
            )

        if markers_scatter:
            for n, marker_date in enumerate(markers_scatter):
                price_location_idx = data.index.get_loc(marker_date, method="nearest")
                # algo to improve text placement of highlight event number
                if (
                    0 < price_location_idx < (len(data) - 1)
                    and data.iloc[price_location_idx - 1]
                    > data.iloc[price_location_idx]
                    and data.iloc[price_location_idx + 1]
                    > data.iloc[price_location_idx]
                ):
                    text_loc = (0, -20)
                else:
                    text_loc = (0, 10)
                ax.annotate(
                    str(n + 1),
                    (mdates.date2num(marker_date), data.iloc[price_location_idx]),
                    xytext=text_loc,
                    textcoords="offset points",
                )
                ax.scatter(
                    marker_date,
                    data.iloc[price_location_idx],
                    color="#00AAFF",
                    s=100,
                )
                fig.add_annotation(
                    x=marker_date,
                    y=data.iloc[price_location_idx],
                    text=str(n + 1),
                    showarrow=False,
                    xshift=text_loc[0],
                    yshift=text_loc[1],
                )
                fig.add_scatter(
                    x=marker_date,
                    y=data.iloc[price_location_idx],
                    mode="markers",
                    marker=dict(color="#00AAFF", size=10),
                    showlegend=False,
                )

    data_type = data.name
    ax.set_ylabel(data_type)
    ax.set_xlim(data.index[0], data.index[-1])
    ax.ticklabel_format(style="plain", axis="y")
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, _: lambda_long_number_format(x))
    )

    if title:
        ax.set_title(title)

    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    fig.show()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "line",
    )


def display_var(
    data: pd.DataFrame,
    symbol: str = "",
    use_mean: bool = False,
    adjusted_var: bool = False,
    student_t: bool = False,
    percentile: float = 99.9,
    data_range: int = 0,
    portfolio: bool = False,
) -> None:
    """Prints table showing VaR of dataframe.

    Parameters
    ----------
    data: pd.Dataframe
        Data dataframe
    use_mean: bool
        if one should use the data mean return
    symbol: str
        name of the data
    adjusted_var: bool
        if one should have VaR adjusted for skew and kurtosis (Cornish-Fisher-Expansion)
    student_t: bool
        If one should use the student-t distribution
    percentile: int
        var percentile
    data_range: int
        Number of rows you want to use VaR over
    portfolio: bool
        If the data is a portfolio
    """

    if data_range > 0:
        df = qa_model.get_var(
            data[-data_range:], use_mean, adjusted_var, student_t, percentile, portfolio
        )
    else:
        df = qa_model.get_var(
            data, use_mean, adjusted_var, student_t, percentile, portfolio
        )

    if adjusted_var:
        str_title = "Adjusted "
    elif student_t:
        str_title = "Student-t "
    else:
        str_title = ""

    if symbol != "":
        symbol += " "

    print_rich_table(
        df,
        show_index=True,
        headers=list(df.columns),
        title=f"[bold]{symbol}{str_title}Value at Risk[/bold]",
        floatfmt=".2f",
    )


def display_es(
    data: pd.DataFrame,
    symbol: str = "",
    use_mean: bool = False,
    distribution: str = "normal",
    percentile: float = 99.9,
    portfolio: bool = False,
) -> None:
    """Prints table showing expected shortfall.

    Parameters
    ----------
    data: pd.DataFrame
        Data dataframe
    use_mean:
        if one should use the data mean return
    symbol: str
        name of the data
    distribution: str
        choose distribution to use: logistic, laplace, normal
    percentile: int
        es percentile
    portfolio: bool
        If the data is a portfolio
    """
    df = qa_model.get_es(data, use_mean, distribution, percentile, portfolio)

    if distribution == "laplace":
        str_title = "Laplace "
    elif distribution == "student_t":
        str_title = "Student-t "
    elif distribution == "logistic":
        str_title = "Logistic "
    else:
        str_title = ""

    if symbol != "":
        symbol += " "

    print_rich_table(
        df,
        show_index=True,
        headers=list(df.columns),
        title=f"[bold]{symbol}{str_title}Expected Shortfall[/bold]",
        floatfmt=".2f",
    )


def display_sharpe(data: pd.DataFrame, rfr: float = 0, window: float = 252) -> None:
    """Plots Calculated the sharpe ratio

    Parameters
    ----------
    data: pd.DataFrame
        selected dataframe column
    rfr: float
        risk free rate
    window: float
        length of the rolling window
    """
    sharpe_ratio = qa_model.get_sharpe(data, rfr, window)

    fig, ax = plt.subplots()
    ax.plot(sharpe_ratio[int(window - 1) :])
    ax.set_title(f"Sharpe Ratio - over a {window} day window")
    ax.set_ylabel("Sharpe ratio")
    ax.set_xlabel("Date")
    fig.legend()
    theme.style_primary_axis(ax)
    theme.visualize_output()

    data = sharpe_ratio[int(window - 1) :]
    fig = OpenBBFigure(yaxis_title="Sharpe Ratio", xaxis_title="Date")
    fig.add_scatter(x=data.index, y=data)
    fig.set_title(f"Sharpe Ratio - over a {window} day window")
    fig.show()


def display_sortino(
    data: pd.DataFrame, target_return: float, window: float, adjusted: bool
) -> None:
    """Plots the sortino ratio

    Parameters
    ----------
    data: pd.DataFrame
        selected dataframe
    target_return: float
        target return of the asset
    window: float
        length of the rolling window
    adjusted: bool
        adjust the sortino ratio
    """
    sortino_ratio = qa_model.get_sortino(data, target_return, window, adjusted)
    if adjusted:
        str_adjusted = "Adjusted "
    else:
        str_adjusted = ""

    fig, ax = plt.subplots()
    ax.plot(sortino_ratio[int(window - 1) :])
    ax.set_title(f"{str_adjusted}Sortino Ratio - over a {window} day window")
    ax.set_ylabel("Sortino ratio")
    ax.set_xlabel("Date")
    fig.legend()

    theme.style_primary_axis(ax)
    theme.visualize_output()

    data = sortino_ratio[int(window - 1) :]
    fig = OpenBBFigure(yaxis=dict(title="Sortino Ratio"))
    fig.add_scatter(x=data.index, y=data)
    fig.set_title(f"Omega Curve - over last {len(data)}'s period")
    fig.show()


def display_omega(
    data: pd.DataFrame, threshold_start: float = 0, threshold_end: float = 1.5
) -> None:
    """Plots the omega ratio

    Parameters
    ----------
    data: pd.DataFrame
        stock dataframe
    threshold_start: float
        annualized target return threshold start of plotted threshold range
    threshold_end: float
        annualized target return threshold end of plotted threshold range
    """
    df = qa_model.get_omega(data, threshold_start, threshold_end)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(df["threshold"], df["omega"])
    ax.set_title(f"Omega Curve - over last {len(data)}'s period")
    ax.set_ylabel("Omega Ratio")
    ax.set_xlabel("Threshold (%)")
    fig.legend()
    ax.set_ylim(threshold_start, threshold_end)

    theme.style_primary_axis(ax)
    theme.visualize_output()
    fig = OpenBBFigure(
        yaxis=dict(title="Omega Ratio"), xaxis=dict(title="Threshold (%)")
    )
    fig.add_scatter(x=df["threshold"], y=df["omega"], name="Omega Curve")
    fig.set_title(f"Omega Curve - over last {len(data)}'s period")
    fig.show()

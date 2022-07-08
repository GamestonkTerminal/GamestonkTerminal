"""Polygon view"""
__docformat__ = "numpy"
import logging
import os

import matplotlib.pyplot as plt

from openbb_terminal.config_terminal import theme
from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal.decorators import check_api_key, log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    lambda_long_number_format,
    print_rich_table,
    plot_autoscale,
)
from openbb_terminal.stocks.fundamental_analysis import polygon_model

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
@check_api_key(["API_POLYGON_KEY"])
def display_fundamentals(
    ticker: str,
    financial: str,
    limit: int = 10,
    quarterly: bool = False,
    ratios: bool = False,
    plot: list = [],
    export: str = "",
):
    """Display tickers balance sheet or income statement

    Parameters
    ----------
    ticker: str
        Stock ticker
    financial:str
        Either balance or income
    limit: int
        Number of results to show, by default 10
    quarterly: bool
        Flag to get quarterly reports, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: list
        List of row labels to plot
    export: str
        Format to export data
    """
    fundamentals = polygon_model.get_financials(ticker, financial, quarterly, ratios)
    title_str = {
        "balance": "Balance Sheet",
        "income": "Income Statement",
        "cash": "Cash Flows",
    }[financial]

    if fundamentals.empty:
        return

    fundamentals = fundamentals.iloc[:, :limit]
    fundamentals = fundamentals[fundamentals.columns[::-1]]

    if plot:
        fundamentals_plot_data = fundamentals.copy().fillna(-1)
        rows_plot = len(plot)
        fundamentals_plot_data = fundamentals_plot_data.transpose()
        fundamentals_plot_data.columns = fundamentals_plot_data.columns.str.lower()
        fundamentals_plot_data.columns = [
            x.replace("_", "") for x in list(fundamentals_plot_data.columns)
        ]

        if rows_plot == 1:
            fig, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
            fundamentals_plot_data[plot[0].replace("_", "")].plot()
            title = (
                f"{plot[0].replace('_', ' ').lower()} {'QoQ' if quarterly else 'YoY'} Growth of {ticker.upper()}"
                if ratios
                else f"{plot[0].replace('_', ' ')} of {ticker.upper()}"
            )
            plt.title(title)
            theme.style_primary_axis(ax)
            theme.visualize_output()
        else:
            fig, axes = plt.subplots(rows_plot)
            for i in range(rows_plot):
                axes[i].plot(fundamentals_plot_data[plot[i].replace("_", "")])
                axes[i].set_title(plot[i].replace("_", " "))
            theme.style_primary_axis(axes[0])
            fig.autofmt_xdate()

    # Snake case to english
    fundamentals.index = fundamentals.index.to_series().apply(
        lambda x: x.replace("_", " ").title()
    )

    # Readable numbers
    fundamentals = fundamentals.applymap(lambda_long_number_format).fillna("-")
    print_rich_table(
        fundamentals.applymap(lambda x: "-" if x == "nan" else x),
        show_index=True,
        title=f"{ticker} {title_str}"
        if not ratios
        else f"{'QoQ' if quarterly else 'YoY'} Change of {ticker} {title_str}",
    )
    export_data(
        export, os.path.dirname(os.path.abspath(__file__)), financial, fundamentals
    )

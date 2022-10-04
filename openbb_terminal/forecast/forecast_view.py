"""Forecast View"""
__docformat__ = "numpy"

import logging
import os
from typing import Dict, Optional, List, Union

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
from darts.utils.statistics import plot_acf

from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    plot_autoscale,
)
from openbb_terminal.helper_funcs import (
    print_rich_table,
)
from openbb_terminal.rich_config import console
from openbb_terminal.forecast import forecast_model
from openbb_terminal.config_terminal import theme
from openbb_terminal.forecast import helpers

logger = logging.getLogger(__name__)

register_matplotlib_converters()


@log_start_end(log=logger)
def show_options(
    datasets: Dict[str, pd.DataFrame],
    dataset_name: str = None,
    export: str = "",
):
    """Plot custom data

    Parameters
    ----------
    datasets: dict
        The loaded in datasets
    dataset_name: str
        The name of the dataset you wish to show options for
    export: str
        Format to export image
    """
    if not datasets:
        console.print(
            "Please load in a dataset by using the 'load' command before using this feature."
        )
    else:
        option_tables = forecast_model.get_options(datasets, dataset_name)

        for dataset, data_values in option_tables.items():
            print_rich_table(
                data_values,
                headers=list(data_values.columns),
                show_index=False,
                title=f"Options for dataset: '{dataset}'",
            )

            export_data(
                export,
                os.path.dirname(os.path.abspath(__file__)),
                f"{dataset}_options",
                data_values.set_index("column"),
            )


@log_start_end(log=logger)
def display_plot(
    data: Union[pd.DataFrame, Dict[str, pd.DataFrame]],
    export: str = "",
    external_axes: Optional[List[plt.axes]] = None,
):
    """Plot data from a dataset
    Parameters
    ----------
    data: Dict[str: pd.DataFrame]
        Dictionary with key being dataset.column and dataframes being values
    export: str
        Format to export image
    external_axes:Optional[List[plt.axes]]
        External axes to plot on
    """
    if isinstance(data, pd.DataFrame):
        data = {col: data[col] for col in data.columns}

    for dataset_col in list(data):
        if isinstance(data[dataset_col].index, pd.MultiIndex):
            console.print(
                "The index appears to be a multi-index. "
                "Therefore, it is not possible to plot the data."
            )
            del data[dataset_col]

    # Check that there's at least a valid dataframe
    if data:
        if external_axes is None:
            _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
        else:
            ax = external_axes[0]

        for dataset_col in data:
            try:
                if isinstance(data[dataset_col], pd.Series):
                    ax.plot(data[dataset_col].index, data[dataset_col].values)
                elif isinstance(data[dataset_col], pd.DataFrame):
                    ax.plot(data[dataset_col])
            except TypeError:
                print(f"Unable to plot column: {dataset_col}")

            theme.style_primary_axis(ax)
            if external_axes is None:
                theme.visualize_output()

        ax.legend(list(data.keys()))

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "plot",
    )


@log_start_end(log=logger)
def display_seasonality(
    data: pd.DataFrame,
    column: str = "close",
    export: str = "",
    m: Optional[int] = None,
    max_lag: int = 24,
    alpha: float = 0.05,
    external_axes: Optional[List[plt.axes]] = None,
):
    """Plot seasonality from a dataset

    Parameters
    ----------
    data: pd.DataFrame
        The dataframe to plot
    column: str
        The column of the dataframe to analyze
    export: str
        Format to export image
    m: Optional[int]
        Optionally, a time lag to highlight on the plot. Default is none.
    max_lag: int
        The maximal lag order to consider. Default is 24.
    alpha: float
        The confidence interval to display. Default is 0.05.
    external_axes:Optional[List[plt.axes]]
        External axes to plot on
    """

    if not data.empty:
        _, series = helpers.get_series(data, column)
        if external_axes is None:
            _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
        else:
            ax = external_axes[0]

        # TODO: Add darts check_seasonality here
        plot_acf(
            series, m=m, max_lag=max_lag, alpha=alpha, axis=ax, default_formatting=False
        )

        theme.style_primary_axis(ax)

        if external_axes is None:
            theme.visualize_output()

    export_data(export, os.path.dirname(os.path.abspath(__file__)), "plot")


@log_start_end(log=logger)
def display_corr(
    dataset: pd.DataFrame,
    export: str = "",
    external_axes: Optional[List[plt.axes]] = None,
):
    """Plot correlation coefficients for dataset features

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset fore calculating correlation coefficients
    export: str
        Format to export image
    external_axes:Optional[List[plt.axes]]
        External axes to plot on
    """

    if external_axes is None:
        _, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    else:
        ax = external_axes[0]

    # correlation
    correlation = forecast_model.corr_df(dataset)
    sns.heatmap(correlation, vmax=1, square=True, annot=True, cmap="cubehelix")
    ax.set_title("Correlation Matrix")
    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()

    export_data(export, os.path.dirname(os.path.abspath(__file__)), "plot")


@log_start_end(log=logger)
def show_df(data: pd.DataFrame, limit: int = 15, name: str = "", export: str = ""):
    console.print(
        f"[green]{name} has following shape (rowxcolumn): {data.shape}[/green]"
    )
    if len(data.columns) > 10:
        console.print(
            "[red]Dataframe has more than 10 columns. Please export"
            " to see all of the data.[/red]\n"
        )
        data = data.iloc[:, :10]
    print_rich_table(
        data.head(limit),
        headers=list(data.columns),
        show_index=True,
        title=f"Dataset {name} | Showing {limit} of {len(data)} rows",
    )

    export_data(
        export, os.path.dirname(os.path.abspath(__file__)), f"{name}_show", data
    )


@log_start_end(log=logger)
def describe_df(data: pd.DataFrame, name: str = "", export: str = ""):
    new_df = forecast_model.describe_df(data)
    print_rich_table(
        new_df,
        headers=list(data.describe().columns),
        show_index=True,
        title=f"Showing Descriptive Statistics for Dataset {name}",
    )

    export_data(export, os.path.dirname(os.path.abspath(__file__)), f"{name}_show")


@log_start_end(log=logger)
def export_df(data: pd.DataFrame, export: str, name: str = "") -> None:
    export_data(
        export, os.path.dirname(os.path.abspath(__file__)), f"{name}_show", data
    )

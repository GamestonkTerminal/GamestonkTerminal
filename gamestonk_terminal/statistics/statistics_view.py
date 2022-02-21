"""Statistics Controller View"""
__docformat__ = "numpy"

import logging
import os
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.config_plot import PLOT_DPI
from gamestonk_terminal.decorators import log_start_end
from gamestonk_terminal.helper_funcs import (
    export_data,
    plot_autoscale,
)
from gamestonk_terminal.rich_config import console
from gamestonk_terminal.statistics import statistics_model
from gamestonk_terminal.helper_funcs import (
    print_rich_table,
)

logger = logging.getLogger(__name__)

register_matplotlib_converters()


@log_start_end(log=logger)
def custom_plot(
    data: pd.DataFrame,
    dataset: str,
    column: str,
    export: str = "",
):
    """Plot custom data

    Parameters
    ----------
    data: pd.DataFrame
        Dataframe of custom data
    dataset: str
        Dataset name
    column: str
        Column for y data
    kind : str
        Kind of plot to pass to pandas plot function
    export: str
        Format to export image
    """
    plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)

    if isinstance(data, pd.Series):
        plt.plot(data)
    elif isinstance(data, pd.DataFrame):
        plt.plot(data[column])

    plt.title(f"{column} data from dataset {dataset}")
    if gtff.USE_ION:
        plt.ion()
    plt.tight_layout()
    plt.show()
    console.print()
    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "custom_plot",
    )


@log_start_end(log=logger)
def display_norm(
    data: pd.DataFrame,
    dataset: str,
    column: str,
    export: str = "",
):
    """Plot custom data

    Parameters
    ----------
    log
    data: pd.DataFrame
        Dataframe of custom data
    dataset: str
        Dataset name
    column: str
        Column for y data
    kind : str
        Kind of plot to pass to pandas plot function
    export: str
        Format to export image
    """

    results = statistics_model.get_normality(data)

    print_rich_table(
        results,
        headers=list(results.columns),
        show_index=True,
        title=f"Normality Test [Column: {column} | Dataset: {dataset}]",
    )

    plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)

    plt.hist(data, bins=100)

    plt.title(f"Histogram of {column} data from dataset {dataset}")
    if gtff.USE_ION:
        plt.ion()
    plt.tight_layout()
    plt.show()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "custom_plot",
    )

    console.print("")


@log_start_end(log=logger)
def display_auto(dependent_variable: pd.Series, residual: pd.DataFrame, export: str = ""):
    """Show autocorrelation tests

    Parameters
    ----------
    model : OLS Model
        Model containing residual values.
    export : str
        Format to export data
    """
    autocorrelation = statistics_model.get_autocorrelation(residual)

    if 1.5 < autocorrelation < 2.5:
        console.print(
            f"The result {autocorrelation} is within the range 1.5 and 2.5 which therefore indicates "
            f"autocorrelation not to be problematic."
        )
    else:
        console.print(
            f"The result {autocorrelation} is outside the range 1.5 and 2.5 and therefore autocorrelation "
            f"can be problematic. Please consider lags of the dependent or independent variable."
        )

    plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    plt.scatter(dependent_variable, residual)
    plt.axhline(y=0, color="r", linestyle="-")
    plt.ylabel("Residual")
    plt.xlabel(dependent_variable.name.capitalize())
    plt.title("Plot of Residuals")

    console.print("")


@log_start_end(log=logger)
def display_granger(time_series_y, time_series_x, lags, confidence_level, export: str = ""):
    """
    """

    granger = statistics_model.get_granger_causality(time_series_y, time_series_x, lags)

    for test in granger[lags][0]:
        # As ssr_chi2test and lrtest have one less value in the tuple, we fill
        # this value with a '-' to allow the conversion to a DataFrame
        if len(granger[lags][0][test]) != 4:
            pars = granger[lags][0][test]
            granger[lags][0][test] = (pars[0], pars[1], "-", pars[2])

    granger_df = pd.DataFrame(granger[lags][0], index=['F-test', 'P-value', 'Count', 'Lags']).T

    print_rich_table(
        granger_df,
        headers=list(granger_df.columns),
        show_index=True,
        title=f"Granger Causality Test [Y: {time_series_y.name} | X: {time_series_x.name} | Lags: {lags}]",
    )

    result_ftest = round(granger[lags][0]['params_ftest'][1], 3)

    if result_ftest > confidence_level:
        console.print(f"As the p-value of the F-test is {result_ftest}, we can not reject the null hypothesis at "
                      f"the {confidence_level} confidence level.")
    else:
        console.print(f"As the p-value of the F-test is {result_ftest}, we can reject the null hypothesis at "
                      f"the {confidence_level} confidence level and find the Series '{time_series_x.name}' "
                      f"to Granger-cause the Series '{time_series_y.name}'")

    console.print("")

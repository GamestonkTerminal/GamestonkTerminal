"""Monte Carlo View"""
__docformat__ = "numpy"

import logging
import os
from typing import List, Optional, Union
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from openbb_terminal.config_terminal import theme
from openbb_terminal.forecast import mc_model, helpers
from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    get_next_stock_market_days,
    plot_autoscale,
    is_valid_axes_count,
)

# pylint: disable=R0913

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_mc_forecast(
    data: Union[pd.DataFrame, pd.Series],
    target_column: str,
    n_future: int,
    n_sims: int,
    use_log=True,
    fig_title: str = "",
    export: str = "",
    time_res: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
):
    """Display monte carlo forecasting

    Parameters
    ----------
    data : Union[pd.Series, np.array]
        Data to forecast
    target_column: str, optional
        The column to select if a dataframe is sent
    n_future : int
        Number of days to forecast
    n_sims : int
        Number of simulations to run
    use_log : bool, optional
        Flag to use lognormal, by default True
    fig_title : str
        Figure title
    export: str
        Format to export data
    time_res : str
        Resolution for data, allowing for predicting outside of standard market days
    external_axes : Optional[List[plt.Axes]], optional
        External axes (2 axes are expected in the list), by default None
    start_date: Optional[datetime]
        The starting date to perform analysis, data before this is trimmed. Defaults to None.
    end_date: Optional[datetime]
        The ending date to perform analysis, data after this is trimmed. Defaults to None.
    """
    data = helpers.clean_data(data, start_date, end_date)
    if "date" in data.columns:
        data = data.set_index("date")
    data = data[target_column]
    predicted_values = mc_model.get_mc_brownian(data, n_future, n_sims, use_log)
    if not time_res or time_res == "1D":
        future_index = get_next_stock_market_days(data.index[-1], n_next_days=n_future)  # type: ignore
    else:
        future_index = pd.date_range(data.index[-1], periods=n_future + 1, freq=time_res)[1:]  # type: ignore

    # This plot has 2 axes
    if external_axes is None:
        _, axes = plt.subplots(1, 2, figsize=plot_autoscale(), dpi=PLOT_DPI)
        (ax1, ax2) = axes
    elif is_valid_axes_count(external_axes, 2):
        (ax1, ax2) = external_axes
    else:
        return

    ax1.plot(data)
    ax1.plot(future_index, predicted_values, alpha=0.3)
    start_timestamp = data.index[0]
    end_timestamp = future_index[-1]
    ax1.set_xlim(start_timestamp, end_timestamp)
    ax1.set_title(f"{fig_title} Data Predictions")

    sns.histplot(predicted_values[-1, :], ax=ax2, kde=True)
    ax2.set_xlabel("Final Value")
    ax2.axvline(
        x=data.values[-1], color=theme.down_color, label="Last Value", linestyle="-"
    )
    ax2.set_title(f"Distribution of final values after {n_future} steps.")
    ax2.set_xlim(np.min(predicted_values[-1, :]), np.max(predicted_values[-1, :]))
    ax2.legend()

    theme.style_primary_axis(ax1)
    theme.style_primary_axis(ax2)
    if external_axes is None:
        theme.visualize_output()

    export_data(export, os.path.dirname(os.path.abspath(__file__)), "mc")

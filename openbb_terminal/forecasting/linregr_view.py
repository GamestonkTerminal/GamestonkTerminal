"""Linear Regression View"""
__docformat__ = "numpy"

import logging
from typing import Union, List

import pandas as pd

from openbb_terminal.forecasting import linregr_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecasting import helpers

logger = logging.getLogger(__name__)
# pylint: disable=too-many-arguments


@log_start_end(log=logger)
def display_linear_regression(
    data: Union[pd.Series, pd.DataFrame],
    ticker_name: str,
    n_predict: int = 5,
    target_col: str = "close",
    past_covariates: str = None,
    train_split: float = 0.85,
    forecast_horizon: int = 5,
    output_chunk_length: int = 1,
    lags: Union[int, List[int]] = 72,
    export: str = "",
    residuals: bool = False,
):
    """Display Linear Regression Forecasting

    Args:
        data (Union[pd.Series, pd.DataFrame]):
            Input Data
        ticker_name str
            The name of the ticker to be predicted
        n_predict (int, optional):
            Days to predict. Defaults to 5.
        target_col (str, optional):
            Target column to forecast. Defaults to "close".
        train_split (float, optional):
            Train/val split. Defaults to 0.85.
        past_covariates (str, optional):
            Multiple secondary columns to factor in when forecasting. Defaults to None.
        forecast_horizon (int, optional):
            Forecast horizon when performing historical forecasting. Defaults to 5.
        output_chunk_length (int, optional):
            The length of the forecast of the model. Defaults to 1.
        lags (int, list)
            lagged target values to predict the next time step
        export: str
            Format to export data
        external_axes : Optional[List[plt.Axes]], optional
            External axes (2 axis is expected in the list), by default None
        residuals: bool
            Whether to show residuals for the model. Defaults to False.
    """
    data["date"] = data["date"].apply(helpers.dt_format)
    (
        ticker_series,
        historical_fcast,
        predicted_values,
        precision,
        _model,
    ) = linregr_model.get_linear_regression_data(
        data,
        n_predict,
        target_col,
        past_covariates,
        train_split,
        forecast_horizon,
        output_chunk_length,
        lags,
    )

    probabilistic = True
    helpers.plot_forecast(
        "LR",
        target_col,
        historical_fcast,
        predicted_values,
        ticker_series,
        ticker_name,
        data,
        n_predict,
        forecast_horizon,
        past_covariates,
        precision,
        probabilistic,
        export,
    )
    if residuals:
        helpers.plot_residuals(
            _model, past_covariates, ticker_series, forecast_horizon=forecast_horizon
        )

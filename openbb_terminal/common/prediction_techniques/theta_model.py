"""Theta Model"""
__docformat__ = "numpy"

import logging
from typing import Any, Tuple, Union

import numpy as np
import pandas as pd
from darts import TimeSeries
from darts.models import Theta
from darts.dataprocessing.transformers import MissingValuesFiller
from darts.utils.utils import SeasonalityMode
from darts.metrics import mape

from openbb_terminal.decorators import log_start_end
from openbb_terminal.rich_config import console

SEASONS = ["N", "A", "M"]
PERIODS = [4, 5, 7]

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_theta_data(
    data: Union[pd.Series, pd.DataFrame],
    seasonal: str = "M",
    seasonal_periods: int = 7,
    n_predict: int = 30,
    start_window: float = 0.65,
    forecast_horizon: int = 3,
) -> Tuple[Any, Any, Any, float, float, Any]:

    """Performs Theta forecasting
    An implementation of the 4Theta method with configurable theta parameter.

    https://unit8co.github.io/darts/generated_api/darts.models.forecasting.theta.html

    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Input data.
    seasonal: str
        Seasonal component.  One of [N, A, M]
        Defaults to MULTIPLICATIVE.
    seasonal_periods: int
        Number of seasonal periods in a year
        If not set, inferred from frequency of the series.
    n_predict: int
        Number of days to forecast
    start_window: float
        Size of sliding window from start of timeseries and onwards
    forecast_horizon: int
        Number of days to forecast when backtesting and retraining historical

    Returns
    -------
    Any
        Adjusted Data series
    Any
        Historical forecast by best theta
    Any
        list of Predictions
    float
        Mean average precision error
    float
        Best Theta
    Any
        Theta Model
    """
    filler = MissingValuesFiller()

    ticker_series = TimeSeries.from_dataframe(
        data,
        time_col="date",
        value_cols=["Close"],
        freq="B",
        fill_missing_dates=True,
    )
    ticker_series = filler.transform(ticker_series).astype(np.float32)
    train, val = ticker_series.split_before(0.85)

    if seasonal == "A":
        seasonal = SeasonalityMode.ADDITIVE
    elif seasonal == "N":
        seasonal = SeasonalityMode.NONE
    else:  # Default
        seasonal = SeasonalityMode.MULTIPLICATIVE

    thetas = np.linspace(-10, 10, 50)
    best_mape = float("inf")
    best_theta = 0
    for theta in thetas:
        model = Theta(
            theta=theta,
            season_mode=seasonal,
            seasonality_period=seasonal_periods,
        )
        model.fit(train)
        pred_theta = model.predict(len(val))
        res = mape(val, pred_theta)
        if res < best_mape:
            best_mape = res
            best_theta = theta

    best_theta_model = Theta(
        best_theta,
        season_mode=seasonal,
        seasonality_period=seasonal_periods,
    )

    console.print(f"Best theta: {best_theta}")
    # Training model based on historical backtesting
    historical_fcast_theta = best_theta_model.historical_forecasts(
        ticker_series,
        start=float(start_window),
        forecast_horizon=int(forecast_horizon),
        verbose=True,
    )

    # fit model on entire series for final prediction
    best_theta_model.fit(ticker_series)
    prediction = best_theta_model.predict(int(n_predict))
    precision = mape(
        actual_series=ticker_series, pred_series=historical_fcast_theta
    )  # mape = mean average precision error
    console.print(f"model {best_theta_model} obtains MAPE: {precision:.2f}% \n")

    return (
        ticker_series,
        historical_fcast_theta,
        prediction,
        precision,
        best_theta,
        best_theta_model,
    )

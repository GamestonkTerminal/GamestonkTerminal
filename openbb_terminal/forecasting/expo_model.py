# pylint: disable=too-many-arguments
"""Probabilistic Exponential Smoothing Model"""
__docformat__ = "numpy"

import logging
from typing import Any, Tuple, Union, List, Optional

import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import pandas as pd
from darts import TimeSeries
from darts.models import ExponentialSmoothing
from darts.utils.utils import ModelMode, SeasonalityMode
from darts.metrics import mape

from openbb_terminal.decorators import log_start_end
from openbb_terminal.rich_config import console
from openbb_terminal.forecasting import helpers


warnings.simplefilter("ignore", ConvergenceWarning)


TRENDS = ["N", "A", "M"]
SEASONS = ["N", "A", "M"]
PERIODS = [4, 5, 7]
DAMPEN = ["T", "F"]

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_expo_data(
    data: Union[pd.Series, pd.DataFrame],
    trend: str = "A",
    seasonal: str = "A",
    seasonal_periods: int = 7,
    dampen: str = "F",
    n_predict: int = 30,
    target_col: str = "close",
    start_window: float = 0.85,
    forecast_horizon: int = 5,
) -> Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], Optional[float], Any]:

    """Performs Probabilistic Exponential Smoothing forecasting
    This is a wrapper around statsmodels Holt-Winters' Exponential Smoothing;
    we refer to this link for the original and more complete documentation of the parameters.

    https://unit8co.github.io/darts/generated_api/darts.models.forecasting.exponential_smoothing.html?highlight=exponential

    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Input data.
    trend: str
        Trend component.  One of [N, A, M]
        Defaults to ADDITIVE.
    seasonal: str
        Seasonal component.  One of [N, A, M]
        Defaults to ADDITIVE.
    seasonal_periods: int
        Number of seasonal periods in a year (7 for daily data)
        If not set, inferred from frequency of the series.
    dampen: str
        Dampen the function
    n_predict: int
        Number of days to forecast
    start_window: float
        Size of sliding window from start of timeseries and onwards
    forecast_horizon: int
        Number of days to forecast when backtesting and retraining historical

    Returns
    -------
    List[float]
        Adjusted Data series
    List[float]
        List of historical fcast values
    List[float]
        List of predicted fcast values
    Optional[float]
        precision
    Any
        Fit Prob. Expo model object.
    """

    use_scalers = False
    _, ticker_series = helpers.get_series(data, target_col, is_scaler=use_scalers)

    if trend == "M":
        trend = ModelMode.MULTIPLICATIVE
    elif trend == "N":
        trend = ModelMode.NONE
    else:  # Default
        trend = ModelMode.ADDITIVE

    if seasonal == "M":
        seasonal = SeasonalityMode.MULTIPLICATIVE
    elif seasonal == "N":
        seasonal = SeasonalityMode.NONE
    else:  # Default
        seasonal = SeasonalityMode.ADDITIVE

    damped = True
    if dampen == "F":
        damped = False

    # Model Init
    model_es = ExponentialSmoothing(
        trend=trend,
        seasonal=seasonal,
        seasonal_periods=int(seasonal_periods),
        damped=damped,
        random_state=42,
    )

    # Historical backtesting
    historical_fcast_es = model_es.historical_forecasts(
        ticker_series,  # backtest on entire ts
        start=float(start_window),
        forecast_horizon=int(forecast_horizon),
        verbose=True,
    )

    # train new model on entire timeseries to provide best current forecast
    best_model = ExponentialSmoothing(
        trend=trend,
        seasonal=seasonal,
        seasonal_periods=int(seasonal_periods),
        damped=damped,
        random_state=42,
    )

    # we have the historical fcast, now lets train on entire set and predict.
    best_model.fit(ticker_series)
    probabilistic_forecast = best_model.predict(int(n_predict), num_samples=500)
    precision = mape(actual_series=ticker_series, pred_series=historical_fcast_es)
    console.print(f"Exponential smoothing obtains MAPE: {precision:.2f}% \n")  # TODO

    return (
        ticker_series,
        historical_fcast_es,
        probabilistic_forecast,
        precision,
        best_model,
    )

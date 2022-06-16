"""Temporal Fusion Transformer View"""
__docformat__ = "numpy"

import logging
from typing import Union

import pandas as pd

from openbb_terminal.forecasting import tft_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecasting import helpers

logger = logging.getLogger(__name__)
# pylint: disable=too-many-arguments


@log_start_end(log=logger)
def display_tft_forecast(
    data: Union[pd.Series, pd.DataFrame],
    ticker_name: str,
    n_predict: int = 30,
    target_col: str = "close",
    past_covariates: str = None,
    train_split: float = 0.85,
    forecast_horizon: int = 5,
    input_chunk_length: int = 14,
    output_chunk_length: int = 5,
    hidden_size: int = 16,
    lstm_layers: int = 1,
    num_attention_heads: int = 4,
    full_attention: bool = False,
    dropout: float = 0.1,
    hidden_continuous_size: int = 8,
    n_epochs: int = 200,
    model_save_name: str = "tft_model",
    force_reset: bool = True,
    save_checkpoints: bool = True,
    export: str = "",
):
    """Display Temporal Fusion Transformer forecast

    Parameters
    ----------
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
    input_chunk_length (int, optional):
        Number of past time steps that are fed to the forecasting module at prediction time.
        Defaults to 14.
    output_chunk_length (int, optional):
        The length of the forecast of the model. Defaults to 5.
    hidden_size (int, optional):
        Hidden state size of the TFT. Defaults to 16.
    lstm_layers (int, optional):
        Number of layers for the Long Short Term Memory Encoder and Decoder. Defaults to 16.
    num_attention_headers (int, optional):
        Number of attention heads. Defaults to 4.
    full_attention (bool, optional):
        Whether to apply a multi-head attention query. Defaults to False>
    dropout (float, optional):
        Fraction of neurons affected by dropout. Defaults to 0.1.
    hidden_continuous_size (int, optional):
        Default hidden size for processing continuous variables. Defaults to 8.
    model_save_name (str, optional):
        The name for the model. Defaults to tft_model
    force_reset (bool, optional):
        If set to True, any previously-existing model with the same name will be reset
        (all checkpoints will be discarded). Defaults to True.
    save_checkpoints (bool, optional):
        Whether or not to automatically save the untrained model and checkpoints from training.
        Defaults to True.
    external_axes : Optional[List[plt.Axes]], optional
        External axes (2 axis is expected in the list), by default None
    """

    # reformat the date column to remove any hour/min/sec
    data["date"] = data["date"].apply(helpers.dt_format)

    (
        ticker_series,
        historical_fcast,
        predicted_values,
        precision,
        _model,
    ) = tft_model.get_tft_data(
        data,
        n_predict,
        target_col,
        past_covariates,
        train_split,
        forecast_horizon,
        input_chunk_length,
        output_chunk_length,
        hidden_size,
        lstm_layers,
        num_attention_heads,
        full_attention,
        dropout,
        hidden_continuous_size,
        n_epochs,
        model_save_name,
        force_reset,
        save_checkpoints,
    )
    probabilistic = True
    helpers.plot_forecast(
        "TFT",
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

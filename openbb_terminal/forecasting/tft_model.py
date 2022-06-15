# pylint: disable=too-many-arguments
"""Temporal Fusion Transformer Model"""
__docformat__ = "numpy"

import logging
from typing import Any, Tuple, Union, List

import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import pandas as pd
from darts import TimeSeries
from darts.models import TFTModel

from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecasting import helpers


warnings.simplefilter("ignore", ConvergenceWarning)


logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_tft_data(
    data: Union[pd.Series, pd.DataFrame],
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
    model_save_name: str = "tft_model",
    force_reset: bool = True,
    save_checkpoints: bool = True,
) -> Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], float, Any]:

    """Performs Temporal Fusion Transformer forecasting
    The TFT applies multi-head attention queries on future inputs from mandatory future_covariates.
    Specifying future encoders with add_encoders (read below) can automatically generate future
    covariates and allows to use the model without having to pass any future_covariates to fit()
    and predict().

    https://unit8co.github.io/darts/generated_api/darts.models.forecasting.tft_model.html

    Parameters
    ----------
    data (Union[pd.Series, pd.DataFrame]):
        Input Data
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



    Returns
    -------
    List[float]
        Adjusted Data series
    List[float]
        List of historical fcast values
    List[float]
        List of predicted fcast values
    float
        precision
    Any
        Fit Prob. Expo model object.
    """
    # TODO add proper doc string
    # TODO Check if torch GPU AVAILABLE
    # TODO add in covariates
    # todo add in all possible parameters for training
    # Export model / save
    # load trained model

    filler, scaler, scaled_ticker_series = helpers.get_series(data, target_col)

    scaled_train, scaled_val = scaled_ticker_series.split_before(float(train_split))

    (
        scaled_past_covariate_whole,
        scaled_past_covariate_train,
        scaled_past_covariate_val,
    ) = helpers.scaled_past_covs(past_covariates, filler, data, train_split)

    my_stopper = helpers.early_stopper(10)

    pl_trainer_kwargs = {"callbacks": [my_stopper], "accelerator": "cpu"}

    nbeats_model = TFTModel(
        input_chunk_length=input_chunk_length,
        output_chunk_length=output_chunk_length,
        hidden_size=hidden_size,
        lstm_layers=lstm_layers,
        num_attention_heads=num_attention_heads,
        full_attention=full_attention,
        dropout=dropout,
        hidden_continuous_size=hidden_continuous_size,
        model_name=model_save_name,
        force_reset=force_reset,
        save_checkpoints=save_checkpoints,
        random_state=42,
        pl_trainer_kwargs=pl_trainer_kwargs,
        add_relative_index=True,
    )

    # fit model on train series for historical forecasting
    helpers.fit_model(
        nbeats_model,
        scaled_train,
        scaled_val,
        scaled_past_covariate_train,
        scaled_past_covariate_val,
    )
    best_model = TFTModel.load_from_checkpoint(model_name=model_save_name, best=True)

    # Showing historical backtesting without retraining model (too slow)
    return helpers.get_prediction(
        scaler,
        past_covariates,
        best_model,
        scaled_ticker_series,
        scaled_past_covariate_whole,
        train_split,
        forecast_horizon,
        n_predict,
        False,
    )

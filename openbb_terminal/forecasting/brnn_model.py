# pylint: disable=too-many-arguments
"""RNN Model"""
__docformat__ = "numpy"

import logging
from typing import Any, Tuple, Union, List, Optional


# import torch
# import torch.nn as nn
# import torch.optim as optim
import pandas as pd

from darts import TimeSeries
from darts.models import BlockRNNModel
from darts.utils.likelihood_models import GaussianLikelihood
from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecasting import helpers

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_brnn_data(
    data: Union[pd.Series, pd.DataFrame],
    n_predict: int = 5,
    target_col: str = "close",
    train_split: float = 0.85,
    past_covariates: str = None,
    forecast_horizon: int = 5,
    input_chunk_length: int = 14,
    output_chunk_length: int = 5,
    model_type: str = "LSTM",
    n_rnn_layers: int = 1,
    hidden_size: int = 20,
    dropout: float = 0.0,
    batch_size: int = 32,
    n_epochs: int = 100,
    learning_rate: float = 1e-3,
    model_save_name: str = "brnn_model",
    force_reset: bool = True,
    save_checkpoints: bool = True,
) -> Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], Optional[float], Any]:
    """Performs Block RNN forecasting

    Args:
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
            Number of past time steps that are fed to the forecasting module at prediction time. Defaults to 14.
        output_chunk_length (int, optional):
            The length of the forecast of the model. Defaults to 5.
        model_type (str, optional):
            Either a string specifying the RNN module type ("RNN", "LSTM" or "GRU"). Defaults to "LSTM".
        n_rnn_layers (int, optional):
             Number of layers in the RNN module. Defaults to 1.
        hidden_size (int, optional):
            Size for feature maps for each hidden RNN layer. Defaults to 20.
        dropout (float, optional):
            Fraction of neurons afected by Dropout. Defaults to 0.0.
        batch_size (int, optional):
            Number of time series (input and output sequences) used in each training pass. Defaults to 32.
        n_epochs (int, optional):
            Number of epochs over which to train the model. Defaults to 100.
        learning_rate (float, optional):
            Defaults to 1e-3.
        model_save_name (str, optional):
            Name for model. Defaults to "brnn_model".
        force_reset (bool, optional):
            If set to True, any previously-existing model with the same name will be reset (all checkpoints will be
            discarded). Defaults to True.
        save_checkpoints (bool, optional):
            Whether or not to automatically save the untrained model and checkpoints from training. Defaults to True.

    Returns:
        List[TimeSeries]
            Adjusted Data series
        List[TimeSeries]
            Historical forecast by best RNN model
        List[TimeSeries]
            list of Predictions
        Optional[float]
            Mean average precision error
        Any
            Best BRNN Model
    """

    # TODO Check if torch GPU AVAILABLE

    use_scalers = True
    probabilistic = False

    filler, scaler, ticker_series = helpers.get_series(
        data, target_col, is_scaler=use_scalers
    )
    train, val = ticker_series.split_before(train_split)
    valid = helpers.check_data_length(
        train, val, input_chunk_length, output_chunk_length
    )
    if not valid:
        return [], [], [], None, None

    (
        past_covariate_whole,
        past_covariate_train,
        past_covariate_val,
    ) = helpers.past_covs(past_covariates, filler, data, train_split, use_scalers)

    # Early Stopping

    brnn_model = BlockRNNModel(
        input_chunk_length=input_chunk_length,
        output_chunk_length=output_chunk_length,
        model=model_type,
        n_rnn_layers=n_rnn_layers,
        hidden_size=hidden_size,
        dropout=dropout,
        batch_size=batch_size,
        n_epochs=n_epochs,
        optimizer_kwargs={"lr": learning_rate},
        model_name=model_save_name,
        random_state=42,
        pl_trainer_kwargs=helpers.get_pl_kwargs(5),
        force_reset=force_reset,
        save_checkpoints=save_checkpoints,
        likelihood=GaussianLikelihood(),
    )

    # fit model on train series for historical forecasting
    helpers.fit_model(
        brnn_model,
        train,
        val,
        past_covariate_train,
        past_covariate_val,
    )
    best_model = BlockRNNModel.load_from_checkpoint(
        model_name=model_save_name, best=True
    )

    # Showing historical backtesting without retraining model (too slow)
    return helpers.get_prediction(
        "Block RNN",
        probabilistic,
        use_scalers,
        scaler,
        past_covariates,
        best_model,
        ticker_series,
        past_covariate_whole,
        train_split,
        forecast_horizon,
        n_predict,
    )

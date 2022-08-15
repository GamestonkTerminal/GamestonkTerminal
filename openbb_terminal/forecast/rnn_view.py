"""RNN View"""
__docformat__ = "numpy"

import logging
from typing import Union, Optional
from datetime import datetime

import pandas as pd

from openbb_terminal.forecast import rnn_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecast import helpers
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)
# pylint: disable=too-many-arguments


@log_start_end(log=logger)
def display_rnn_forecast(
    data: Union[pd.DataFrame, pd.Series],
    target_column: str = "close",
    dataset_name: str = "",
    n_predict: int = 5,
    train_split: float = 0.85,
    forecast_horizon: int = 5,
    model_type: str = "LSTM",
    hidden_dim: int = 20,
    dropout: float = 0.0,
    batch_size: int = 16,
    n_epochs: int = 100,
    learning_rate: float = 1e-3,
    model_save_name: str = "rnn_model",
    training_length: int = 20,
    input_chunk_size: int = 14,
    force_reset: bool = True,
    save_checkpoints: bool = True,
    export: str = "",
    residuals: bool = False,
    forecast_only: bool = False,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    naive: bool = False,
):
    """Display RNN forecast

    Parameters
    ----------
        data (Union[pd.Series, pd.DataFrame]):
            Input Data
        dataset_name str
            The name of the ticker to be predicted
        n_predict (int, optional):
            Days to predict. Defaults to 5.
        target_column (str, optional):
            Target column to forecast. Defaults to "close".
        train_split (float, optional):
            Train/val split. Defaults to 0.85.
        forecast_horizon (int, optional):
            Forecast horizon when performing historical forecasting. Defaults to 5.
        model_type (str, optional):
            Either a string specifying the RNN module type ("RNN", "LSTM" or "GRU"). Defaults to "LSTM".
        hidden_dim (int, optional):
            Size for feature maps for each hidden RNN layer.. Defaults to 20.
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
            If set to True, any previously-existing model with the same name will be reset
            (all checkpoints will be discarded). Defaults to True.
        save_checkpoints (bool, optional):
            Whether or not to automatically save the untrained model and checkpoints from training. Defaults to True.
        forecast_only: bool
            Whether to only show dates in the forecasting range. Defaults to False.
        export: str
            Format to export data
        residuals: bool
            Whether to show residuals for the model. Defaults to False.
        start_date: Optional[datetime]
            The starting date to perform analysis, data before this is trimmed. Defaults to None.
        end_date: Optional[datetime]
            The ending date to perform analysis, data after this is trimmed. Defaults to None.
        naive: bool
            Whether to show the naive baseline. This just assumes the closing price will be the same
            as the previous day's closing price. Defaults to False.
    """

    data = helpers.clean_data(data, start_date, end_date)
    if not helpers.check_data(data, target_column):
        console.print(
            f"[red]Column {target_column} is not in the dataframe."
            " Change the 'target_column' parameter.[/red]\n"
        )
        return
    (
        ticker_series,
        historical_fcast,
        predicted_values,
        precision,
        _model,
    ) = rnn_model.get_rnn_data(
        data=data,
        n_predict=n_predict,
        target_column=target_column,
        train_split=train_split,
        forecast_horizon=forecast_horizon,
        model_type=model_type,
        hidden_dim=hidden_dim,
        dropout=dropout,
        batch_size=batch_size,
        n_epochs=n_epochs,
        learning_rate=learning_rate,
        model_save_name=model_save_name,
        training_length=training_length,
        input_chunk_size=input_chunk_size,
        force_reset=force_reset,
        save_checkpoints=save_checkpoints,
    )
    if ticker_series == []:
        return

    past_covariates = None
    probabilistic = True
    helpers.plot_forecast(
        "RNN",
        target_column,
        historical_fcast,
        predicted_values,
        ticker_series,
        dataset_name,
        data,
        n_predict,
        forecast_horizon,
        past_covariates,
        precision,
        probabilistic,
        export,
        forecast_only=forecast_only,
        naive=naive,
    )
    if residuals:
        helpers.plot_residuals(
            _model, past_covariates, ticker_series, forecast_horizon=forecast_horizon
        )

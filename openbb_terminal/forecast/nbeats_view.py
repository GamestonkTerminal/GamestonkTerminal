"""NBEATS View"""
__docformat__ = "numpy"

import logging
from typing import Union, Optional
from datetime import datetime

import pandas as pd

from openbb_terminal.forecast import nbeats_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.forecast import helpers

logger = logging.getLogger(__name__)
# pylint: disable=too-many-arguments


@log_start_end(log=logger)
def display_nbeats_forecast(
    data: Union[pd.DataFrame, pd.Series],
    target_column: str = "close",
    dataset_name: str = "",
    n_predict: int = 5,
    past_covariates: str = None,
    train_split: float = 0.85,
    forecast_horizon: int = 5,
    input_chunk_length: int = 14,
    output_chunk_length: int = 5,
    num_stacks: int = 10,
    num_blocks: int = 3,
    num_layers: int = 4,
    layer_widths: int = 512,
    n_epochs: int = 100,
    learning_rate: float = 1e-3,
    batch_size: int = 800,
    model_save_name: str = "nbeats_model",
    force_reset: bool = True,
    save_checkpoints: bool = True,
    export: str = "",
    residuals: bool = False,
    forecast_only: bool = False,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    naive: bool = False,
):
    """Display NBEATS forecast

    Parameters
    ----------
        data (Union[pd.Series, pd.DataFrame]):
            Input Data
        target_column (str, optional):
            Target column to forecast. Defaults to "close".
        dataset_name str
            The name of the ticker to be predicted
        n_predict (int, optional):
            Days to predict. Defaults to 5.
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
        num_stacks (int, optional):
            The number of stacks that make up the whole model. Defaults to 10.
        num_blocks (int, optional):
            The number of blocks making up every stack. Defaults to 3.
        num_layers (int, optional):
            The number of fully connected layers preceding the final forking layers in each block
            of every stack. Defaults to 4.
        layer_widths (int, optional):
            Determines the number of neurons that make up each fully connected layer in each block
            of every stack. Defaults to 512.
        batch_size (int, optional):
            Number of time series (input and output sequences) used in each training pass. Defaults
            to 32.
        n_epochs (int, optional):
            Number of epochs over which to train the model. Defaults to 100.
        learning_rate (float, optional):
            Defaults to 1e-3.
        model_save_name (str, optional):
            Name for model. Defaults to "brnn_model".
        force_reset (bool, optional):
            If set to True, any previously-existing model with the same name will be reset (all
            checkpoints will be discarded). Defaults to True.
        save_checkpoints (bool, optional):
            Whether or not to automatically save the untrained model and checkpoints from training.
            Defaults to True.
        export: str
            Format to export data
        residuals: bool
            Whether to show residuals for the model. Defaults to False.
        forecast_only: bool
            Whether to only show dates in the forecasting range. Defaults to False.
        start_date: Optional[datetime]
            The starting date to perform analysis, data before this is trimmed. Defaults to None.
        end_date: Optional[datetime]
            The ending date to perform analysis, data after this is trimmed. Defaults to None.
        naive: bool
            Whether to show the naive baseline. This just assumes the closing price will be the same
            as the previous day's closing price. Defaults to False.
    """

    data = helpers.clean_data(data, start_date, end_date)
    (
        ticker_series,
        historical_fcast,
        predicted_values,
        precision,
        _model,
    ) = nbeats_model.get_NBEATS_data(
        data=data,
        n_predict=n_predict,
        target_column=target_column,
        past_covariates=past_covariates,
        train_split=train_split,
        forecast_horizon=forecast_horizon,
        input_chunk_length=input_chunk_length,
        output_chunk_length=output_chunk_length,
        num_stacks=num_stacks,
        num_blocks=num_blocks,
        num_layers=num_layers,
        layer_widths=layer_widths,
        batch_size=batch_size,
        n_epochs=n_epochs,
        learning_rate=learning_rate,
        model_save_name=model_save_name,
        force_reset=force_reset,
        save_checkpoints=save_checkpoints,
    )
    if ticker_series == []:
        return

    probabilistic = False
    helpers.plot_forecast(
        "NBEATS",
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

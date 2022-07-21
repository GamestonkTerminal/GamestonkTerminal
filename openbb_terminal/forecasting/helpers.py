# pylint: disable=too-many-arguments
import os
import argparse
from typing import Dict, Any, Union, Optional, List
from datetime import timedelta
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    mean_squared_error,
)
from darts.dataprocessing.transformers import MissingValuesFiller, Scaler
from darts.utils.statistics import plot_residuals_analysis
from darts import TimeSeries
from darts.metrics import mape
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from openbb_terminal.rich_config import console
from openbb_terminal import config_neural_network_models as cfg
from openbb_terminal.config_terminal import theme
from openbb_terminal.helper_funcs import (
    export_data,
    plot_autoscale,
    print_rich_table,
    is_valid_axes_count,
)
from openbb_terminal.config_plot import PLOT_DPI
from openbb_terminal import rich_config

logger = logging.getLogger(__name__)


def mean_absolute_percentage_error(y_true: np.ndarray, y_pred: np.ndarray) -> np.number:
    """Calculate mean absolute percent error"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def print_prediction_kpis(real: np.ndarray, pred: np.ndarray):
    """Print prediction statistics"""
    kpis = {
        "MAPE": f"{mean_absolute_percentage_error(real, pred) :.3f} %",
        "R2": f"{r2_score(real, pred) :.3f}",
        "MAE": f"{mean_absolute_error(real, pred):.3f}",
        "MSE": f"{mean_squared_error(real, pred):.3f}",
        "RMSE": f"{mean_squared_error(real, pred, squared=False):.3f}",
    }
    df = pd.DataFrame.from_dict(kpis, orient="index")
    print_rich_table(
        df,
        show_index=True,
        title="KPIs",
        floatfmt=".2f",
    )


def plot_data_predictions(
    data,
    preds,
    y_valid,
    y_dates_valid,
    scaler,
    title,
    forecast_data,
    n_loops,
    time_str: str = "",
    external_axes: Optional[List[plt.Axes]] = None,
):
    """Plots data predictions for the different ML techniques
    external_axes : Optional[List[plt.Axes]], optional
        External axes (1 axis is expected in the list), by default None
    """

    # This plot has 1 axis
    if external_axes is None:
        _, ax = plt.subplots(
            figsize=plot_autoscale(),
            dpi=PLOT_DPI,
        )
    elif is_valid_axes_count(external_axes, 1):
        (ax,) = external_axes
    else:
        return

    ax.plot(
        data.index,
        data.values,
        "-o",
        ms=2,
        label="Real data",
    )
    for i in range(len(y_valid) - 1):

        if scaler:
            y_pred = scaler.inverse_transform(preds[i].reshape(-1, 1)).ravel()
            y_act = scaler.inverse_transform(y_valid[i].reshape(-1, 1)).ravel()
        else:
            y_pred = preds[i].ravel()
            y_act = y_valid[i].ravel()
        ax.plot(
            y_dates_valid[i],
            y_pred,
            color=theme.down_color,
        )
        ax.fill_between(
            y_dates_valid[i],
            y_pred,
            y_act,
            where=(y_pred < y_act),
            color=theme.down_color,
            alpha=0.2,
        )
        ax.fill_between(
            y_dates_valid[i],
            y_pred,
            y_act,
            where=(y_pred > y_act),
            color=theme.up_color,
            alpha=0.2,
        )

    # Leave this out of the loop so that the legend doesn't get overpopulated with "Predictions"
    if scaler:
        final_pred = scaler.inverse_transform(preds[-1].reshape(-1, 1)).ravel()
        final_valid = scaler.inverse_transform(y_valid[-1].reshape(-1, 1)).ravel()
    else:
        final_pred = preds[-1].reshape(-1, 1).ravel()
        final_valid = y_valid[-1].reshape(-1, 1).ravel()
    ax.plot(
        y_dates_valid[-1],
        final_pred,
        color=theme.down_color,
        label="Predictions",
    )
    ax.fill_between(
        y_dates_valid[-1],
        final_pred,
        final_valid,
        alpha=0.2,
    )

    _, _, ymin, ymax = plt.axis()
    ax.vlines(
        forecast_data.index[0],
        ymin,
        ymax,
        linestyle="--",
    )
    if n_loops == 1:
        ax.plot(
            forecast_data.index,
            forecast_data.values,
            "-o",
            label="Forecast",
        )
    else:
        ax.plot(
            forecast_data.index,
            forecast_data.median(axis=1).values,
            "-o",
            label="Forecast",
        )
        ax.fill_between(
            forecast_data.index,
            forecast_data.quantile(0.25, axis=1).values,
            forecast_data.quantile(0.75, axis=1).values,
            alpha=0.3,
        )
    # Subtracting 1 day only works nicely for daily data.  For now if not daily, then start line on last point
    if not time_str or time_str == "1D":
        ax.axvspan(
            forecast_data.index[0] - timedelta(days=1),
            forecast_data.index[-1],
            alpha=0.2,
        )
        ax.set_xlim(data.index[0], forecast_data.index[-1] + timedelta(days=1))

    else:
        ax.axvspan(
            forecast_data.index[0],
            forecast_data.index[-1],
            alpha=0.2,
        )
        ax.set_xlim(data.index[0], forecast_data.index[-1])
    ax.set_title(title)
    ax.legend()
    ax.set_ylabel("Value")

    theme.style_primary_axis(ax)

    if external_axes is None:
        theme.visualize_output()


def prepare_scale_train_valid_test(
    data: Union[pd.DataFrame, pd.Series],
    n_input_days: int,
    n_predict_days: int,
    test_size: float,
    s_end_date: str,
    no_shuffle: bool,
):
    """
    Prepare and scale train, validate and test data.
    Parameters
    ----------
    data: pd.DataFrame
        Dataframe of stock prices
    ns_parser: argparse.Namespace
        Parsed arguments
    Returns
    -------
    X_train: np.ndarray
        Array of training data.  Shape (# samples, n_inputs, 1)
    X_test: np.ndarray
        Array of validation data.  Shape (total sequences - #samples, n_inputs, 1)
    y_train: np.ndarray
        Array of training outputs.  Shape (#samples, n_days)
    y_test: np.ndarray
        Array of validation outputs.  Shape (total sequences -#samples, n_days)
    X_dates_train: np.ndarray
        Array of dates for X_train
    X_dates_test: np.ndarray
        Array of dates for X_test
    y_dates_train: np.ndarray
        Array of dates for y_train
    y_dates_test: np.ndarray
        Array of dates for y_test
    test_data: np.ndarray
        Array of prices after the specified end date
    dates_test: np.ndarray
        Array of dates after specified end date
    scaler:
        Fitted PREPROCESSOR
    """

    # Pre-process data
    if cfg.Preprocess == "standardization":
        scaler = StandardScaler()

    elif cfg.Preprocess == "minmax":
        scaler = MinMaxScaler()

    elif cfg.Preprocess == "normalization":
        scaler = Normalizer()

    elif (cfg.Preprocess == "none") or (cfg.Preprocess is None):
        scaler = None
    # Test data is used for forecasting.  Takes the last n_input_days data points.
    # These points are not fed into training

    if s_end_date:
        data = data[data.index <= s_end_date]
        if n_input_days + n_predict_days > data.shape[0]:
            console.print(
                "Cannot train enough input days to predict with loaded dataframe\n"
            )
            return (
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                True,
            )

    test_data = data.iloc[-n_input_days:]
    train_data = data.iloc[:-n_input_days]

    dates = data.index
    dates_test = test_data.index
    if scaler:
        train_data = scaler.fit_transform(data.values.reshape(-1, 1))
        test_data = scaler.transform(test_data.values.reshape(-1, 1))
    else:
        train_data = data.values.reshape(-1, 1)
        test_data = test_data.values.reshape(-1, 1)

    prices = train_data

    input_dates = []
    input_prices = []
    next_n_day_prices = []
    next_n_day_dates = []

    for idx in range(len(prices) - n_input_days - n_predict_days):
        input_prices.append(prices[idx : idx + n_input_days])  # noqa: E203
        input_dates.append(dates[idx : idx + n_input_days])  # noqa: E203
        next_n_day_prices.append(
            prices[
                idx + n_input_days : idx + n_input_days + n_predict_days  # noqa: E203
            ]
        )
        next_n_day_dates.append(
            dates[
                idx + n_input_days : idx + n_input_days + n_predict_days  # noqa: E203
            ]
        )

    input_dates = np.asarray(input_dates)  # type: ignore
    input_prices = np.array(input_prices)  # type: ignore
    next_n_day_prices = np.array(next_n_day_prices)  # type: ignore
    next_n_day_dates = np.asarray(next_n_day_dates)  # type: ignore

    (
        X_train,
        X_valid,
        y_train,
        y_valid,
        X_dates_train,
        X_dates_valid,
        y_dates_train,
        y_dates_valid,
    ) = train_test_split(
        input_prices,
        next_n_day_prices,
        input_dates,
        next_n_day_dates,
        test_size=test_size,
        shuffle=no_shuffle,
    )
    return (
        X_train,
        X_valid,
        y_train,
        y_valid,
        X_dates_train,
        X_dates_valid,
        y_dates_train,
        y_dates_valid,
        test_data,
        dates_test,
        scaler,
        False,
    )


def lambda_price_prediction_color(val: float, last_val: float) -> str:
    """Set prediction to be a colored string"""
    if float(val) > last_val:
        return f"[green]$ {val:.2f} [/green]"
    return f"[red]$ {val:.2f} [/red]"


def print_pretty_prediction(df_pred: pd.DataFrame, last_price: float):
    """Print predictions"""
    if rich_config.USE_COLOR:
        df_pred = pd.DataFrame(df_pred)
        df_pred.columns = ["pred"]
        df_pred["pred"] = df_pred["pred"].apply(
            lambda x: lambda_price_prediction_color(x, last_val=last_price)
        )
        print_rich_table(
            df_pred,
            show_index=True,
            index_name="Datetime",
            headers=["Prediction"],
            floatfmt=".2f",
            title=f"Actual price: [yellow]$ {last_price:.2f} [/yellow]",
        )


def past_covs(past_covariates, filler, data, train_split, is_scaler=True):
    if past_covariates is not None:
        covariates_scalers = []  # to hold all temp scalers in case we need them
        target_covariates_names = past_covariates.split(",")

        # create first covariate to then stack onto
        console.print(f"[green]Covariate #0: {target_covariates_names[0]}[/green]")
        if is_scaler:
            past_covariate_scaler = Scaler()
            past_covariate_whole = past_covariate_scaler.fit_transform(
                filler.transform(
                    TimeSeries.from_dataframe(
                        data,
                        time_col="date",
                        value_cols=target_covariates_names[0],
                        freq="B",
                        fill_missing_dates=True,
                    )
                )
            ).astype(np.float32)
        else:
            past_covariate_whole = filler.transform(
                TimeSeries.from_dataframe(
                    data,
                    time_col="date",
                    value_cols=target_covariates_names[0],
                    freq="B",
                    fill_missing_dates=True,
                )
            ).astype(np.float32)

        if len(target_covariates_names) > 1:
            for i, column in enumerate(target_covariates_names[1:]):
                console.print(f"[green]Covariate #{i+1}: {column}[/green]")
                if is_scaler:
                    _temp_scaler = Scaler()
                    covariates_scalers.append(_temp_scaler)
                    _temp_new_covariate = _temp_scaler.fit_transform(
                        filler.transform(
                            TimeSeries.from_dataframe(
                                data,
                                time_col="date",
                                value_cols=[column],
                                freq="B",
                                fill_missing_dates=True,
                            )
                        )
                    ).astype(np.float32)
                else:
                    _temp_new_covariate = filler.transform(
                        TimeSeries.from_dataframe(
                            data,
                            time_col="date",
                            value_cols=[column],
                            freq="B",
                            fill_missing_dates=True,
                        )
                    ).astype(np.float32)

                # continually stack covariates based on column names
                past_covariate_whole = past_covariate_whole.stack(_temp_new_covariate)

        # Split the full scale covariate to train and val
        (
            past_covariate_train,
            past_covariate_val,
        ) = past_covariate_whole.split_before(train_split)
        return (
            past_covariate_whole,
            past_covariate_train,
            past_covariate_val,
        )
    else:
        return None, None, None


def early_stopper(patience: int, monitor: str = "train_loss"):
    my_stopper = EarlyStopping(
        monitor=monitor,
        patience=patience,
        min_delta=0,
        mode="min",
    )
    return my_stopper


def get_pl_kwargs(
    patience: int, monitor: str = "train_loss", accelerator: str = "cpu"
) -> Dict[str, Any]:
    my_stopper = early_stopper(5, "train_loss")
    pl_trainer_kwargs = {"callbacks": [my_stopper], "accelerator": "cpu"}
    return pl_trainer_kwargs


def plot_forecast(
    name: str,
    target_col: str,
    historical_fcast,
    predicted_values,
    ticker_series,
    ticker_name: str,
    data,
    n_predict: int,
    forecast_horizon,
    past_covariates,
    precision,
    probabilistic,
    export: str,
    low_quantile: float = None,
    high_quantile: float = None,
    forecast_only: bool = False,
):
    quant_kwargs = {}
    if low_quantile:
        quant_kwargs["low_quantile"] = low_quantile
    if high_quantile:
        quant_kwargs["high_quantile"] = high_quantile
    external_axes = None
    if not external_axes:
        fig, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
    else:
        if len(external_axes) != 1:
            logger.error("Expected list of one axis item.")
            console.print("[red]Expected list of one axis item.\n[/red]")
            return
        ax = external_axes

    # ax = fig.get_axes()[0] # fig gives list of axes (only one for this case)
    if forecast_only:
        ticker_series = ticker_series.drop_before(historical_fcast.start_time())
    ticker_series.plot(label=target_col, figure=fig)
    historical_fcast.plot(
        label=f"Backtest {forecast_horizon}-Steps ahead forecast",
        figure=fig,
        **quant_kwargs,
    )

    pred_label = f"{name} Forecast"
    if past_covariates:
        pred_label += f" w/ past covs({past_covariates})"
    predicted_values.plot(label=pred_label, figure=fig, **quant_kwargs)
    ax.set_title(
        f"{name} for ${ticker_name} for next [{n_predict}] days (MAPE={precision:.2f}%)"
    )
    ax.set_ylabel(target_col)
    ax.set_xlabel("Date")
    theme.style_primary_axis(ax)

    if not external_axes:
        theme.visualize_output()

    if probabilistic:
        numeric_forecast = predicted_values.quantile_df()[f"{target_col}_0.5"].tail(
            n_predict
        )
    else:
        numeric_forecast = predicted_values.pd_dataframe()[target_col].tail(n_predict)

    print_pretty_prediction(numeric_forecast, data[target_col].iloc[-1])

    export_data(export, os.path.dirname(os.path.abspath(__file__)), "expo")


def dt_format(x):
    """Convert any Timestamp to YYYY-MM-DD
    Args:
        x: Pandas Timestamp of any length
    Returns:
        x: formatted string
    """
    x = pd.to_datetime(x)
    x = x.strftime("%Y-%m-%d")
    return x


def get_series(data, target_col: str = None, is_scaler: bool = True):
    filler = MissingValuesFiller()
    filler_kwargs = dict(
        df=data,
        time_col="date",
        value_cols=[target_col],
        freq="B",
        fill_missing_dates=True,
    )
    try:
        ticker_series = TimeSeries.from_dataframe(**filler_kwargs)
    except ValueError:
        # remove business days to allow base lib to assume freq
        filler_kwargs.pop("freq")
        ticker_series = TimeSeries.from_dataframe(**filler_kwargs)

    if is_scaler:
        scaler = Scaler()
        scaled_ticker_series = scaler.fit_transform(
            filler.transform(ticker_series)
        ).astype(np.float32)
        return filler, scaler, scaled_ticker_series
    ticker_series = filler.transform(ticker_series).astype(np.float32)
    scaler = None
    return filler, scaler, ticker_series


def fit_model(
    model,
    series,
    val_series=None,
    past_covariates=None,
    val_past_covariates=None,
    **kwargs,
):
    fit_kwargs = dict(
        series=series,
    )
    fit_kwargs.update(kwargs)
    if val_series is not None:
        fit_kwargs["val_series"] = val_series
    if past_covariates is not None:
        fit_kwargs["past_covariates"] = past_covariates
        fit_kwargs["val_past_covariates"] = val_past_covariates

    model.fit(**fit_kwargs)


def get_prediction(
    model_name,
    probabilistic,
    use_scalers,
    scaler,
    past_covariates,
    best_model,
    ticker_series,
    past_covariate_whole,
    train_split,
    forecast_horizon,
    n_predict: int,
):
    # Historical backtest if with covariates
    if past_covariates is not None:
        historical_fcast = best_model.historical_forecasts(
            ticker_series,
            past_covariates=past_covariate_whole,
            start=train_split,
            forecast_horizon=forecast_horizon,
            retrain=False,
            verbose=True,
        )
    # historical backtest without covariates
    else:
        historical_fcast = best_model.historical_forecasts(
            ticker_series,
            start=train_split,
            forecast_horizon=forecast_horizon,
            retrain=False,
            verbose=True,
        )

    # now predict N days in the future
    if past_covariates is not None:
        if probabilistic:
            prediction = best_model.predict(
                series=ticker_series,
                past_covariates=past_covariate_whole,
                n=n_predict,
                num_samples=500,
            )
        else:
            prediction = best_model.predict(
                series=ticker_series,
                past_covariates=past_covariate_whole,
                n=n_predict,
            )
    else:
        if probabilistic:
            prediction = best_model.predict(
                series=ticker_series, n=n_predict, num_samples=500
            )
        else:
            prediction = best_model.predict(series=ticker_series, n=n_predict)

    precision = mape(
        actual_series=ticker_series, pred_series=historical_fcast
    )  # mape = mean average precision error
    console.print(f"{model_name} model obtains MAPE: {precision:.2f}% \n")

    # scale back
    if use_scalers:
        ticker_series = scaler.inverse_transform(ticker_series)
        historical_fcast = scaler.inverse_transform(historical_fcast)
        prediction = scaler.inverse_transform(prediction)

    return ticker_series, historical_fcast, prediction, precision, best_model


def check_parser_input(parser: argparse.ArgumentParser, datasets, *args) -> bool:
    # check proper file name is provided
    if not hasattr(parser, "target_dataset"):
        return False
    if not parser.target_dataset:  # type: ignore
        console.print("[red]Please enter valid dataset.\n[/red]")
        return False
    if "ignore_column" in args:
        return True
    if not hasattr(parser, "target_column"):
        return False

    # must check that target col is within target series
    if parser.target_column not in datasets[parser.target_dataset].columns:  # type: ignore
        console.print(
            f"[red]The column {parser.target_column} does not exist.\n[/red]"  # type: ignore
        )
        return False
    return True


def plot_residuals(
    model, past_covariates, series, forecast_horizon: int = 1, num_bins: int = 20
):
    if past_covariates:
        console.print(
            "[red]Cannot calculate and plot residuals if there are past covariates.[/red]"
        )
    else:
        console.print(
            "[green]Calculating and plotting residuals... This may take a few moments.[/green]"
        )
        my_stopper = early_stopper(5, "train_loss")
        pl_trainer_kwargs = {"callbacks": [my_stopper], "accelerator": "cpu"}
        model.pl_trainer_kwargs = pl_trainer_kwargs
        residuals = model.residuals(
            series=series, forecast_horizon=forecast_horizon, verbose=True
        )
        plot_residuals_analysis(residuals=residuals, num_bins=num_bins, fill_nan=True)

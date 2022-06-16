"""Arima Prediction Model"""
__docformat__ = "numpy"

import logging
from typing import Any, List, Tuple, Union, Optional

import pandas as pd
import pmdarima
from statsmodels.tsa.arima.model import ARIMA

from openbb_terminal.decorators import log_start_end
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)

ICS = ["aic", "aicc", "bic", "hqic", "oob"]


@log_start_end(log=logger)
def get_arima_model(
    values: Union[pd.Series, pd.DataFrame],
    arima_order: str,
    n_predict: int,
    seasonal: bool,
    ic: str,
) -> Tuple[Optional[List[float]], Optional[Any]]:
    """Get an ARIMA model for data

    Parameters
    ----------
    values : Union[pd.Series, pd.DataFrame]
        Data to fit
    arima_order : str
        String of ARIMA params in form "p,q,d"
    n_predict : int
        Days to predict
    seasonal : bool
        Flag to use seasonal model
    ic : str
        Information Criteria for model evaluation

    Returns
    -------
    List[float]
        List of predicted values
    Any
        Fit ARIMA model object.
    """
    if arima_order:
        model = ARIMA(
            values, order=tuple(int(ord) for ord in arima_order.split(","))
        ).fit()
        l_predictions = list(
            model.predict(
                start=len(values.values) + 1,
                end=len(values.values) + n_predict,
            )
        )
        return l_predictions, model
    kwargs = {}
    if seasonal:
        kwargs["m"] = 5
    try:
        model = pmdarima.auto_arima(
            values.values,
            error_action="ignore",
            seasonal=False,
            information_criteria=ic,
            **kwargs
        )
    except ValueError:
        console.print(
            "[red]Column must be convertible to float (no words or dates)[/red]"
        )
        return None, None

    l_predictions = list(model.predict(n_predict))

    return l_predictions, model

from datetime import datetime
import pandas as pd
from openbb_terminal.forecasting import arima_view as av


def test_display_arima(tsla_csv):
    av.display_arima(
        dataset="Data",
        values=tsla_csv,
        target_column="close",
        arima_order="1,2,3",
        n_predict=1,
        seasonal=True,
        ic="aic",
        results=True,
    )

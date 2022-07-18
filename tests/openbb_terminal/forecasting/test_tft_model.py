from openbb_terminal.forecasting import tft_model
from tests.openbb_terminal.forecasting import conftest


def test_get_tft_model(tsla_csv):
    conftest.test_model(tft_model.get_tft_data, tsla_csv, n_epochs=1)

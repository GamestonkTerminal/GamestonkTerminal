from openbb_terminal.forecasting import brnn_model
from tests.openbb_terminal.forecasting import conftest


def test_get_brnn_model(tsla_csv):
    conftest.test_model(brnn_model.get_brnn_data, tsla_csv, n_epochs=1)

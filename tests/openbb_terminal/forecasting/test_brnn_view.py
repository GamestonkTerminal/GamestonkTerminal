from openbb_terminal.forecasting import brnn_view


def test_display_brnn_forecast(tsla_csv, mocker):
    mock = mocker.patch("openbb_terminal.forecasting.trans_view.helpers.plot_residuals")
    brnn_view.display_brnn_forecast(tsla_csv, "TSLA",  n_epochs=1, residuals=True)
    mock.assert_called_once()

from openbb_terminal.forecast import tft_view


def test_display_tft_forecast(tsla_csv, mocker):
    mock = mocker.patch("openbb_terminal.forecast.trans_view.helpers.plot_residuals")
    tft_view.display_tft_forecast(tsla_csv, forecast_horizon=1, residuals=True)
    mock.assert_called_once()

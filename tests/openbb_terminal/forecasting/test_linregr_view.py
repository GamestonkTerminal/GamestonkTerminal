from openbb_terminal.forecasting import linregr_view


def test_display_linregr_forecast(tsla_csv, mocker):
    mock = mocker.patch("openbb_terminal.forecasting.trans_view.helpers.plot_residuals")
    linregr_view.display_linear_regression(tsla_csv, "TSLA", residuals=True)
    mock.assert_called_once()

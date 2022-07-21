from openbb_terminal.forecasting import regr_view


def test_display_regr_forecast(tsla_csv, mocker):
    mock = mocker.patch("openbb_terminal.forecasting.trans_view.helpers.plot_residuals")
    regr_view.display_regression(tsla_csv, "TSLA", residuals=True)
    mock.assert_called_once()

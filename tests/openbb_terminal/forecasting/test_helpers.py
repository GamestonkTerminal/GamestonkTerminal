import numpy as np
from openbb_terminal.forecasting import helpers


def test_mean_absolute_percentage_error():
    arr = np.array([1, 2, 3, 4])
    assert helpers.mean_absolute_percentage_error(arr, arr) == 0


def test_print_prediction_kpis():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([2, 3, 4, 5])
    helpers.print_prediction_kpis(arr1, arr2)

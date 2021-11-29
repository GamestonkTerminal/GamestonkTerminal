"""Regression Model"""
__docformat__ = "numpy"
from typing import Tuple, List, Any, Union
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import pipeline
from sklearn import preprocessing

# The tsxv dependence was removed so this fails.  Taking from didiers source


def split_train(
    sequence: np.ndarray, numInputs: int, numOutputs: int, numJumps: int
) -> Tuple[List, List]:
    """Returns sets to train a model
        i.e. X[0] = sequence[0], ..., sequence[numInputs]
             y[0] = sequence[numInputs+1], ..., sequence[numInputs+numOutputs]
             ...
             X[k] = sequence[k*numJumps], ..., sequence[k*numJumps+numInputs]
             y[k] = sequence[k*numJumps+numInputs+1], ..., sequence[k*numJumps+numInputs+numOutputs]

    Parameters:
        sequence (array)  : Full training dataset
        numInputs (int)   : Number of inputs X used at each training
        numOutputs (int)  : Number of outputs y used at each training
        numJumps (int)    : Number of sequence samples to be ignored between (X,y) sets
    Returns:
        X (2D array): Array of numInputs arrays.
                      len(X[k]) = numInputs
        y (2D array): Array of numOutputs arrays
                      len(y[k]) = numOutputs
    """

    X: List = []
    y: List = []

    if numInputs + numOutputs > len(sequence):
        print(
            "To have at least one X,y arrays, the sequence size needs to be bigger than numInputs+numOutputs"
        )
        return X, y

    for i in range(len(sequence)):
        i = numJumps * i
        end_ix = i + numInputs

        # Once train data crosses time series length return
        if end_ix + numOutputs > len(sequence):
            break

        seq_x = sequence[i:end_ix]
        X.append(seq_x)
        seq_y = sequence[end_ix : end_ix + numOutputs]
        y.append(seq_y)

    return X, y


def get_regression_model(
    values: Union[pd.Series, pd.DataFrame],
    poly_order: int,
    n_input: int,
    n_predict: int,
    n_jumps: int,
) -> Tuple[List[float], Any]:
    """Fit regression model of variable order

    Parameters
    ----------
    values : Union[pd.Series, pd.DataFrame]
        Data to fit
    poly_order : int
        Order of polynomial
    n_input : int
        Length of input sequence
    n_predict : int
        Length of prediction sequence
    n_jumps : int
        Number of jumps in data preparation

    Returns
    -------
    List[float]
        List of predicted values
    Any
        Linear model fit to data
    """
    # Split training data
    stock_x, stock_y = split_train(
        values.values,
        n_input,
        n_predict,
        n_jumps,
    )

    if not stock_x:
        print("Given the model parameters more training data is needed.\n")
        return [], None

    # Machine Learning model
    if poly_order == 1:
        model = linear_model.LinearRegression(n_jobs=-1)
    else:
        model = pipeline.make_pipeline(
            preprocessing.PolynomialFeatures(poly_order), linear_model.Ridge()
        )

    model.fit(stock_x, stock_y)
    l_predictions = [
        i if i > 0 else 0
        for i in model.predict(values.values[-n_input:].reshape(1, -1))[0]
    ]
    return l_predictions, model

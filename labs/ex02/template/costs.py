# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np


def compute_loss(y, tx, w):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE

    n = len(y)
    e = y - tx.dot(w)

    # Rename function to mse or mae based on what you want
    return compute_mse(e)

    # TODO: compute loss by MSE
    # ***************************************************
    raise NotImplementedError


def compute_mse(e):
    """Calculate the loss using MSE.

    Args:
        e: numpy array of shape=(N, )

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    loss = e.dot(e)/(2*len(e))
    return loss

    # TODO: compute loss by MSE
    # ***************************************************


def compute_mae(e):
    """Calculate the loss using MAE.

    Args:
        e: numpy array of shape=(N, )

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE

    loss = np.mean(np.abs(e))
    return loss

    # TODO: compute loss by MAE
    # ***************************************************

# *_* coding:utf-8 *_*
import numpy as np

def rnn_cell_forward(da_next,cache):
    """
    Implements the backward pass for the RNN-cell (single time-step).

    Arguments:
    da_next -- Gradient of loss with respect to next hidden state
    cache -- python dictionary containing useful values (output of rnn_cell_forward())

    Returns:
    gradients -- python dictionary containing:
                        dx -- Gradients of input data, of shape (n_x, m)
                        da_prev -- Gradients of previous hidden state, of shape (n_a, m)
                        dWax -- Gradients of input-to-hidden weights, of shape (n_a, n_x)
                        dWaa -- Gradients of hidden-to-hidden weights, of shape (n_a, n_a)
                        dba -- Gradients of bias vector, of shape (n_a, 1)
    """

    # Retrieve values from cache
    (a_next,a_prev,xt,parameters) = cache

    # Retrieve values from parameters
    Wax = parameters["Wax"]
    Waa = parameters["Waa"]
    Wya = parameters["Wya"]
    ba = parameters["ba"]
    by = parameters["by"]

    ### START CODE HERE ###
    # compute the gradient of tanh with respect to a_next (≈1 line)
    dtanh = np.tanh(a_next)**2
    # compute the gradient of the loss with respect to Wax (≈2 lines)
    dxt = np.dot(np.transpose(Wax),(1-np.tanh(np.dot(Wax,xt)+np.dot(Waa,a_prev)+ba)**2))
    dWax = np.dot((1-np.tanh(np.dot(Wax,xt)+np.dot(Waa,a_prev)+ba)**2),np.transpose(xt))

    # compute the gradient with respect to Waa (≈2 lines)
    da_prev = np.dot(np.transpose(Waa),1-np.tanh(np.dot(Wax,)))
    dWaa = None

    # compute the gradient with respect to b (≈1 line)
    dba = None

    ### END CODE HERE ###

    # Store the gradients in a python dictionary
    gradients = {"dxt": dxt, "da_prev": da_prev, "dWax": dWax, "dWaa": dWaa, "dba": dba}

    return gradients
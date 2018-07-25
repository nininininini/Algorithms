# *_* coding:utf-8 *_*
import numpy as np


# GRADED FUNCTION: run_cell_forward
def rnn_cell_forward(xt,a_prev,parameters):
    """
    Implements a single forward step of the RNN-cell as described in Figure (2)

    Arguments:
    xt -- your input data at timestep "t", numpy array of shape (n_x, m).
    a_prev -- Hidden state at timestep "t-1", numpy array of shape (n_a, m)
    parameters -- python dictionary containing:
                        Wax -- Weight matrix multiplying the input, numpy array of shape (n_a, n_x)
                        Waa -- Weight matrix multiplying the hidden state, numpy array of shape (n_a, n_a)
                        Wya -- Weight matrix relating the hidden-state to the output, numpy array of shape (n_y, n_a)
                        ba --  Bias, numpy array of shape (n_a, 1)
                        by -- Bias relating the hidden-state to the output, numpy array of shape (n_y, 1)
    Returns:
    a_next -- next hidden state, of shape (n_a, m)
    yt_pred -- prediction at timestep "t", numpy array of shape (n_y, m)
    cache -- tuple of values needed for the backward pass, contains (a_next, a_prev, xt, parameters)
    """
    # Retrieve parameters from "parameters"
    Wax = parameters['Wax']
    Waa = parameters['Waa']
    Wya = parameters['Wya']
    ba = parameters['ba']
    by = parameters['by']

    ### START CODE HERE ###
    # compute next activation state using the formula given above
    mutil = np.dot(Waa,a_prev)+np.dot(Wax,xt)+ba
    a_next = (np.exp(mutil)-np.exp(-mutil))/(np.exp(mutil)+np.exp(-mutil))
    # compute output of the current cell using the formula given above
    para = np.dot(Wya,a_next)+by
    # print(np.sum(np.exp(para),axis=0))
    yt_pred = np.exp(para)/np.sum(np.exp(para),axis=0)
    ### END CODE HERE

    # store values you need for backward propagation in cache
    cache = (a_next,a_prev,xt,parameters)

    return a_next,yt_pred,cache

if __name__=="__main__":
    np.random.seed(1)
    xt = np.random.randn(3,10)
    a_prev = np.random.randn(5,10)
    Waa = np.random.randn(5,5)
    Wax = np.random.randn(5,3)
    Wya = np.random.randn(2,5)
    ba = np.random.randn(5,1)
    by = np.random.randn(2,1)
    # print(a_prev)
    parameters = {"Waa":Waa,"Wax":Wax,"Wya":Wya,"ba":ba,"by":by}
    a_next,yt_pred,cache = rnn_cell_forward(xt,a_prev,parameters)
    print("a_next[4] =", a_next[4])
    print("a_next.shape =", a_next.shape)
    print("yt_pred[1] =", yt_pred[1])
    print("yt_pred.shape ", yt_pred.shape)


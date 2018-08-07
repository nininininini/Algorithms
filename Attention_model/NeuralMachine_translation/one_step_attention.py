# _*_ coding:utf-8 _*_

from keras.layers import RepeatVector,Concatenate

# GRADED FUNCTION: one_step_attention

def one_step_attention(a,s_prev):
    """
    Performs one step of attention: Outputs a context vector computed as a dot product of the attention weights
    "alphas" and the hidden states "a" of the Bi-LSTM.

    Arguments:
    a -- hidden state output of the Bi-LSTM, numpy-array of shape (m, Tx, 2*n_a)
    s_prev -- previous hidden state of the (post-attention) LSTM, numpy-array of shape (m, n_s)

    Returns:
    context -- context vector, input of the next (post-attetion) LSTM cell
    """

    ### START CODE HERE ###
    # Use repeator to repeat s_prev to be of shape (m,Tx,n_s) so that you can concatenate it with all hidden states "a"
    s_prev = RepeatVector(s_prev)
    # Use concatenator to concatenate a and s_prev on the last axis (≈ 1 line)
    concat = Concatenate(a)
    # Use densor1 to propagate concat through a small fully-connected neural network to compute the "intermediate energies" variable e. (≈1 lines)
    e = None
    # Use densor2 to propagate e through a small fully-connected neural network to compute the "energies" variable energies. (≈1 lines)
    energies = None
    # Use "activator" on "energies" to compute the attention weights "alphas" (≈ 1 line)
    alphas = None
    # Use dotor together with "alphas" and "a" to compute the context vector to be given to the next (post-attention) LSTM-cell (≈ 1 line)
    context = None
    ### END CODE HERE ###

    return context

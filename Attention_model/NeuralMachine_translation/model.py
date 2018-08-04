# _*_ coding:utf-8 _*_

from keras.layers import Input
# GRADED FUNCTION: model
Tx = 30
Ty = 10

def model(Tx, Ty, n_a, n_s, human_vocab_size, machine_vocab_size):
    """
    Arguments:
    Tx -- length of the input sequence
    Ty -- length of the output sequence
    n_a -- hidden state size of the Bi-LSTM
    n_s -- hidden state size of the post-attention LSTM
    human_vocab_size -- size of the python dictionary "human_vocab"
    machine_vocab_size -- size of the python dictionary "machine_vocab"

    Returns:
    model -- Keras model instance
    """

    # Define the inputs of your model with a shape (Tx,)
    # Define s0 and c0, initial hidden state for the decoder LSTM of shape (n_s,)
    X = Input(shape=(Tx, human_vocab_size))
    s0 = Input(shape=(n_s,), name='s0')
    c0 = Input(shape=(n_s,), name='c0')
    s = s0
    c = c0

    # Initialize empty list of outputs
    outputs = []
    ### START CODE HERE ###

    # Step 1: Define your pre-attention Bi-LSTM. Remember to use return_sequences=True. (≈ 1 line)
    a = None

    # Step 2: Iterate for Ty steps
    for t in range(None):
        # Step 2.A: Perform one step of the attention mechanism to get back the context vector at step t (≈ 1 line)
        context = None

        # Step 2.B: Apply the post-attention LSTM cell to the "context" vector.
        # Don't forget to pass: initial_state = [hidden state, cell state] (≈ 1 line)
        s, _, c = None

        # Step 2.C: Apply Dense layer to the hidden state output of the post-attention LSTM (≈ 1 line)
        out = None

        # Step 2.D: Append "out" to the "outputs" list (≈ 1 line)
        None

    # Step 3: Create model instance taking three inputs and returning the list of outputs. (≈ 1 line)
    model = None

    ### END CODE HERE ###

    return model

if __name__ == "__main__":
    model = model(Tx, Ty, n_a, n_s, len(human_vocab), len(machine_vocab))
    model.summary()
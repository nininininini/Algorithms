# *_* coding:utf-8 *_*

import numpy as np
from Natural_languange_processing.WordVectors import w2v_function as w2v
from Natural_languange_processing.WordVectors import cosine_similarity  as cosine

words, word_to_vec_map = w2v.read_glove_vecs('data/glove.6B.50d.txt')

def neutralize(word,g,word_to_vec_map):
    """
    Removes the bias of "word" by projecting it on the space orthogonal to the bias axis.
    This function ensures that gender neutral words are zero in the gender subspace.

    Arguments:
        word -- string indicating the word to debias
        g -- numpy-array of shape (50,), corresponding to the bias axis (such as gender)
        word_to_vec_map -- dictionary mapping words to their corresponding vectors.

    Returns:
        e_debiased -- neutralized word vector representation of the input "word"
    """

    ### START CODE HERE ###
    # Select word vector representation of "word". Use word_to_vec_map. (≈ 1 line)
    e = word_to_vec_map[word]
    # Compute e_biascomponent using the formula give above. (≈ 1 line)
    e_biascomponent =np.dot(e,g)/(np.sum(g**2))*g

    # Neutralize e by substracting e_biascomponent from it
    # e_debiased should be equal to its orthogonal projection. (≈ 1 line)
    e_debiased = e - e_biascomponent
    ### END CODE HERE ###

    return e_debiased

if __name__ == "__main__":
    g = word_to_vec_map['woman'] - word_to_vec_map['man']
    e = "receptionist"
    print("cosine similarity between " + e + " and g, before neutralizing: ",
          cosine.cosine_similarity(word_to_vec_map["receptionist"], g))

    e_debiased = neutralize("receptionist", g, word_to_vec_map)
    print("cosine similarity between " + e + " and g, after neutralizing: ", cosine.cosine_similarity(e_debiased, g))
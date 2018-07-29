# _*_ coding:utf-8 _*_

import numpy as np
from Natural_languange_processing.WordVectors import w2v_function as w2v

words,word_to_vec_map = w2v.read_glove_vecs("data/glove.6B.50d.txt")

# GRADED FUNCTION: cosine_similarity
def cosine_similarity(u,v):
    """
    Cosine similarity reflects the degree of similariy between u and v

    Arguments:
        u -- a word vector of shape (n,)
        v -- a word vector of shape (n,)

    Returns:
        cosine_similarity -- the cosine similarity between u and v defined by the formula above.
    """

    distance = 0.0

    ### START CODE HERE ###
    # Compute the dot product between u and v (≈1 line)
    dot = np.dot(u,v)
    # Compute the L2 norm of u (≈1 line)
    norm_u = np.sqrt(np.sum(u**2))

    # Compute the L2 norm of v (≈1 line)
    norm_v = np.sqrt(np.sum(v**2))
    # Compute the cosine similarity defined by formula (1) (≈1 line)
    cosine_similarity = dot/(norm_u*norm_v)
    ### END CODE HERE ###

    return cosine_similarity

if __name__=="__main__":
    father = word_to_vec_map["father"]
    mother = word_to_vec_map["mother"]
    ball = word_to_vec_map["ball"]
    crocodile = word_to_vec_map["crocodile"]
    france = word_to_vec_map["france"]
    italy = word_to_vec_map["italy"]
    paris = word_to_vec_map["paris"]
    rome = word_to_vec_map["rome"]

    print("cosine_similarity(father, mother) = ", cosine_similarity(father, mother))
    print("cosine_similarity(ball, crocodile) = ", cosine_similarity(ball, crocodile))
    print("cosine_similarity(france - paris, rome - italy) = ", cosine_similarity(france - paris, rome - italy))

# *_* coding:utf-8 *_*
import numpy as np
from Natural_languange_processing.WordVectors import w2v_function as w2v
from Natural_languange_processing.WordVectors import cosine_similarity  as cosine

words, word_to_vec_map = w2v.read_glove_vecs('data/glove.6B.50d.txt')
# GRADED FUNCTION: complete_analogy
def equalize(pair,bias_axis,word_to_vec_map):
    """
    Debias gender specific words by following the equalize method described in the figure above.

    Arguments:
    pair -- pair of strings of gender specific words to debias, e.g. ("actress", "actor")
    bias_axis -- numpy-array of shape (50,), vector corresponding to the bias axis, e.g. gender
    word_to_vec_map -- dictionary mapping words to their corresponding vectors

    Returns
    e_1 -- word vector corresponding to the first word
    e_2 -- word vector corresponding to the second word
    """

    ### START CODE HERE ###
    # Step 1: Select word vector representation of "word". Use word_to_vec_map. (≈ 2 lines)
    w1, w2 = pair
    e_w1, e_w2 = word_to_vec_map[w1],word_to_vec_map[w2]

    # Step 2: Compute the mean of e_w1 and e_w2 (≈ 1 line)
    mu = (e_w1+e_w2)/2

    # Step 3: Compute the projections of mu over the bias axis and the orthogonal axis (≈ 2 lines)
    mu_B = np.dot(mu,bias_axis)/np.sum(bias_axis**2)*bias_axis
    mu_orth = mu-mu_B

    # Step 4: Use equations (7) and (8) to compute e_w1B and e_w2B (≈2 lines)
    e_w1B = np.dot(e_w1,bias_axis)/np.sum(bias_axis**2)*bias_axis
    e_w2B = np.dot(e_w2,bias_axis)/np.sum(bias_axis**2)*bias_axis

    # Step 5: Adjust the Bias part of e_w1B and e_w2B using the formulas (9) and (10) given above (≈2 lines)
    corrected_e_w1B = np.sqrt(np.abs(1-np.sum(mu_orth**2)))*(e_w1B-mu_B)/np.abs((e_w1-mu_orth)-mu_B)
    corrected_e_w2B = np.sqrt(np.abs(1-np.sum(mu_orth**2)))*(e_w2B-mu_B)/np.abs((e_w2-mu_orth)-mu_B)

    # Step 6: Debias by equalizing e1 and e2 to the sum of their corrected projections (≈2 lines)
    e1 = corrected_e_w1B+mu_orth
    e2 = corrected_e_w2B+mu_orth

    ### END CODE HERE ###

    return e1, e2

if __name__=="__main__":
    g = word_to_vec_map['woman'] - word_to_vec_map['man']
    print("cosine similarities before equalizing:")
    print("cosine_similarity(word_to_vec_map[\"man\"], gender) = ", cosine.cosine_similarity(word_to_vec_map["man"], g))
    print("cosine_similarity(word_to_vec_map[\"woman\"], gender) = ", cosine.cosine_similarity(word_to_vec_map["woman"], g))
    print()
    e1, e2 = equalize(("man", "woman"), g, word_to_vec_map)
    print("cosine similarities after equalizing:")
    print("cosine_similarity(e1, gender) = ", cosine.cosine_similarity(e1, g))
    print("cosine_similarity(e2, gender) = ", cosine.cosine_similarity(e2, g))
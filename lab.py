# coding: utf-8
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.stats import pearsonr
from util import preprocess_text, parse_sts
import argparse


def w2v_sentence_mean(sent, word2vec):
    """Creates a sentence representation by taking the mean of all in-vocabulary word vectors.
    Returns None if no words are in vocabulary."""
    toks = preprocess_text(sent)
    veclist = [word2vec[tok] for tok in toks if tok in word2vec]
    if len(veclist) == 0:
        return None
    mean_vec = np.mean(veclist, axis=0)
    return mean_vec

def w2v_sentence_product(sent, word2vec):
    """Creates a sentence representation by taking the mean of all in-vocabulary word vectors.
    Returns None if no words are in vocabulary."""
    toks = preprocess_text(sent)
    veclist = [word2vec[tok] for tok in toks if tok in word2vec]
    if len(veclist) == 0:
        return None
    prod_vec = np.product(veclist, axis=0)
    return prod_vec


def main(sts_dev, w2v_file):
    # TODO 1: load the texts
    dev_texts, dev_y = parse_sts(sts_dev)

    # TODO 2: load word2vec using gensim KeyedVectors object
    w2v_vecs = KeyedVectors.load_word2vec_format(w2v_file, binary=False)

    # TODO 3: Define the functions above that compose word representations into sentence representations
    # TODO 4: get cosine similarities of every sentence pair in dev
    # if either sentence is completely out of vocabulary, record "0" as the similarity
    cos_sims_mean = []

    # means first
    for t1,t2 in dev_texts:
        t1_vector_mean = w2v_sentence_mean(t1, w2v_vecs)
        if t1_vector_mean is None:
            cos_sims_mean.append(0)
            continue
        t1_vector_mean = t1_vector_mean.reshape((1, -1)) # shape for cosine similarity
        t2_vector_mean = w2v_sentence_mean(t2, w2v_vecs)
        if t2_vector_mean is None:
            cos_sims_mean.append(0)
            continue
        t2_vector_mean = t2_vector_mean.reshape((1, -1))
        pair_similarity = cosine_similarity(t1_vector_mean, t2_vector_mean)[0, 0]
        cos_sims_mean.append(pair_similarity)

    # now products
    cos_sims_product = []
    for t1, t2 in dev_texts:
        t1_vector_product = w2v_sentence_product(t1, w2v_vecs)
        if t1_vector_product is None:
            cos_sims_product.append(0)
            continue
        t1_vector_product = t1_vector_product.reshape((1, -1)) # shape for cosine similarity
        t2_vector_product = w2v_sentence_product(t2, w2v_vecs)
        if t2_vector_product is None:
            cos_sims_product.append(0)
            continue
        t2_vector_product = t2_vector_product.reshape((1, -1))
        pair_similarity = cosine_similarity(t1_vector_product, t2_vector_product)[0, 0]
        cos_sims_product.append(pair_similarity)

    # TODO 5: Measure correlation with STS labels for the two ways of computing word2vec sentence representations
    pearson_mean = pearsonr(cos_sims_mean, dev_y)
    print(f"word2vec mean pearsons: r={pearson_mean[0]:.03}")

    pearson_prod = pearsonr(cos_sims_product, dev_y)
    print(f"word2vec product pearsons: r={pearson_prod[0]:.03}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="../strings_for_similarity/stsbenchmark/sts-dev.csv",
                        help="tab separated sts data in benchmark format")
    parser.add_argument("--w2v_file", type=str, default="50K_GoogleNews_vecs.txt",
                        help="text format word2vec embeddings")
    args = parser.parse_args()

    main(args.sts_data, args.w2v_file)

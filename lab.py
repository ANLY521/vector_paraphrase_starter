# coding: utf-8
from util import preprocess_text, parse_sts
import argparse


def w2v_sentence_mean(sent, word2vec):
    """Creates a sentence representation by taking the mean of all in-vocabulary word vectors.
    Returns None if no words are in vocabulary."""
    return None

def w2v_sentence_product(sent, word2vec):
    """Creates a sentence representation by taking the mean of all in-vocabulary word vectors.
    Returns None if no words are in vocabulary."""
    return None


def main(sts_dev, w2v_file):
    # load the texts
    dev_texts, dev_y = parse_sts(sts_dev)

    # load word2vec using gensim KeyedVectors object
    w2v_vecs = None

    # get cosine similarities of every pair in dev
    # if either sentence is completely out of vocabulary, record "0" as the similarity
    cos_sims_mean = []
    cos_sims_product = []

    pearson_mean = 0
    print(f"word2vec mean pearsons: r={pearson_mean[0]:.03}")

    pearson_prod = 0
    print(f"word2vec product pearsons: r={pearson_prod[0]:.03}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="../strings_for_similarity/stsbenchmark/sts-dev.csv",
                        help="tab separated sts data in benchmark format")
    parser.add_argument("--w2v_file", type=str, default="50K_GoogleNews_vecs.txt",
                        help="text format word2vec embeddings")
    args = parser.parse_args()

    main(args.sts_data, args.w2v_file)

import argparse

class SimilarityVectorizer:
    """Creates a vector of similarities for pairs of sentences"""

    def __init__(self, idf_corpus, word2vec_file):
        """
        Instantiates SimilarityVectorizer. Loads word2vec and calculates IDF.
        :param idf_corpus: list of strings; documents to learn inverse document frequency
        :param word2vec_file: path to .txt formatted word2vec vectors
        """


    def tfidf_sim(self, t1, t2):
        """Takes two strings. Returns a float of cosine similarity between tfidf vectors"""

        return 0

    def w2v_sim(self, t1, t2):
        """Takes two strings. Returns a float of cosine similarity between w2v vectors for two sentences.
        w2v vectors are the mean of any in-vocabulary words in the sentence.
        Cosine similarity is 0 if either sentence is completely out of vocabulary. """

        return 0

    def bleu_sim(self, t1, t2):
        """Takes two strings. Returns sum of BLEU using each as reference and hypothesis"""

        return 0

    def load_X(self, sent_pairs):
        """Create a matrix where every row represents a pair of sentences and every column in a feature.
        """
        X = None

        return X



def main(sts_train_file, sts_dev_file, w2v_file):
    """Fits a logistic regression for paraphrase identification, using string similarity metrics and vector similarity
    as features. Prints results on held-out data. Data is formatted as in the STS benchmark"""

    max_nonparaphrase = 3.0
    min_paraphrase = 4.0




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_dev_file", type=str, default="../strings_for_similarity/stsbenchmark/sts-dev.csv",
                        help="dev file")
    parser.add_argument("--sts_train_file", type=str, default="../strings_for_similarity/stsbenchmark/sts-train.csv",
                        help="train file")
    parser.add_argument("--w2v_file", type=str, default="50K_GoogleNews_vecs.txt",
                        help="file with word2vec vectors as text")
    args = parser.parse_args()

    main(args.sts_train_file, args.sts_dev_file, args.w2v_file)

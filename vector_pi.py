import argparse
from util import parse_sts, sts_to_pi

class SimilarityVectorizer:
    """Creates a vector of similarities for pairs of sentences"""

    def __init__(self, idf_corpus, word2vec_file):
        """
        Instantiates SimilarityVectorizer. Loads word2vec and calculates IDF.
        :param idf_corpus: list of strings; documents to learn inverse document frequency
        :param word2vec_file: path to .txt formatted word2vec vectors
        """

        self.w2v_vectors = None # set this attribute to a KeyedVectors instance with loaded weights

        self.tfidf_vectorizer = None # set this attribute to a tfidf vectorizer that is fit to idf_corpus


    def tfidf_sim(self, t1, t2):
        """Takes two strings. Returns a float of cosine similarity between tfidf vectors
        Uses self.tfidf_vectorizer"""

        return 0

    def w2v_sim(self, t1, t2):
        """Takes two strings. Returns a float of cosine similarity between w2v vectors for two sentences.
        w2v vectors are the mean of any in-vocabulary words in the sentence.
        Cosine similarity is 0 if either sentence is completely out of vocabulary.
         Uses self.w2v_vectors"""

        return 0

    def bleu_sim(self, t1, t2):
        """Takes two strings. Returns sum of BLEU using each as reference and hypothesis"""

        return 0

    def wer_sim(self, t1, t2):
        """Takes two strings. Returns sum of word error rate using each as reference and hypothesis"""

        return 0

    def transform(self, sent_pairs):
        """Creates a matrix where every row represents a pair of sentences and every column in a similarity feature.
        Features are [bleu, wer, tfidf similarity, w2v similarity].
        """
        X = None

        return X



def main(sts_train_file, sts_dev_file, w2v_file):
    """Fits a logistic regression for paraphrase identification, using string similarity metrics and vector similarity
    as features. Prints results on held-out data. Data is formatted as in the STS benchmark"""

    min_paraphrase = 4.0
    max_nonparaphrase = 3.0

    # TODO 1: Load data partitions and convert to paraphrase dataset as in the lab
    # You will train a logistic regression on the TRAIN partition
    train_texts_sts, train_y_sts = parse_sts(sts_train_file)

    # You will evaluate predictions on the VALIDATION partition
    dev_texts_sts, dev_y_sts = parse_sts(sts_dev_file)


    # TODO 2: instantiate a SimilarityVectorizer object. Complete the stubbed methods in the class def above

    # TODO 3: use the SimilarityVectorizer object to convert sentence pairs into feature representations


    # TODO 4: Train a logistic regression model using sklearn.linear_model.LogisticRegression
    # Hint: The interface is very similar to other sklearn models we have used in class

    # TODO 5: Evaluate your logistic regression model using accuracy, precision, recall and F1
    # Get predictions for the dev partition to do this



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

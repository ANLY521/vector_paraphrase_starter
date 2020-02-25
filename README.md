Paraphrase Identification using vector space models
---------------------------------------------------

This project examines vector space similarity for paraphrase identification.
It converts semantic textual similarity data to paraphrase identification data using threshholds.

Data is from the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).




## `50K_GoogleNews_vecs.txt`

Download [here](https://drive.google.com/file/d/1VKz_8FFTQebHIL-Ok_Qo63rwhR6dbu4G/view?usp=sharing).

A truncated version of the 300-vectors trained by Google Research on an enormous corpus of Google News.
Only the first 50K are circulated here to reduce memory and disk usage; 
the full file is available at <https://code.google.com/archive/p/word2vec/> .

## `lab.py`

`lab.py` calculates the pearsons correlation of word2vec vectors and the STS paraphrase dataset.
It tests two ways of creating sentence vectors: mean and product of in-vocubulary words.

Example usage:

`python lab.py --sts_data stsbenchmark/sts-dev.csv`


## `vector_pi.py`

* Train a logistic regression for PI on the training data using three features: cosine similarity over
 two different vector spaces (mean word2vec and term frequency) and BLEU. 
* Create a `SimilarityVectorizer` class that implements each of the three similarities as methods, 
and that has a method `load_X` that returns a matrix of similarities for a list of sentence pairs.
* Set a gensim `KeyedVectors` object and a `TfidfVectorizer` object as attributes to your `SimilarityVectorizer`
and use them in methods.
* Stem the tokens for TFIDF but not for Word2Vec. Remove punctuation and stopwords for both vector methods.
* Lowercase the inputs to all three similarity calculations.
* Use the logistic regression implementation in `sklearn`.
* Update the results with your precision, recall and F1 on the development set.

## Results

Report your results here.

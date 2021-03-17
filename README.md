Paraphrase Identification using vector space models
---------------------------------------------------

This project examines vector space similarity for paraphrase identification.
It converts semantic textual similarity data to paraphrase identification data using threshholds.

Data is from the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).


## Results

TODO: Write up your results for the experiments from this and the previous homework:
* Complete the table by adding results from last week and this week.
* Define the features used in featureset 1 (last homework) and featureset 2 (this homework)
* Analyze your results, at least 3 sentences

Precise results will vary a little based on preprocessing choices.


| Model Name | Accuracy | Precision | Recall | F1|
| ---------- | -------- | --------- | ------- | ---|
| TFIDF cosine sim| ...
| Logistic regression, featureset 1
| Logistic regression, featureset 2 


TODO: Define featuresets 1 and 2 from the table

TODO: Analyze results in table


## `50K_GoogleNews_vecs.txt`

Download [here](https://drive.google.com/file/d/1VKz_8FFTQebHIL-Ok_Qo63rwhR6dbu4G/view?usp=sharing).

This homework uses a truncated version of the 300-vectors trained by Google Research on an enormous corpus of Google News.
Only the first 50K are circulated for class to reduce memory and disk usage. 
It's more common to use a much larger vocabulary size. 
the full file is available at <https://code.google.com/archive/p/word2vec/> .

**DO NOT TRY TO CHECK THIS DATA INTO GIT** 

## `lab.py`

`lab.py` calculates the pearsons correlation of word2vec vectors and the STS paraphrase dataset.
It tests two ways of creating sentence vectors: mean and product of in-vocubulary words.

Example usage:

`python lab.py --sts_data stsbenchmark/sts-dev.csv`


## `vector_pi.py`

**WARNING:** you may need to downgrade gensim:
`conda install gensim==3.4`

* Train a logistic regression for paraphrase identification on the training data using four features:
    - BLEU
    - WER
    - Cosine Similarity of TFIDF vectors
    - Cosine Similarity of w2v vectors
* Use the logistic regression implementation in `sklearn`.
* Update the readme as described in *Results*.

`python vector_pi.py --sts_dev_file stsbenchmark/sts-dev.csv --sts_train_file stsbenchmark/sts-train.csv`

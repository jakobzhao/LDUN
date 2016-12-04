tutorial

https://rare-technologies.com/word2vec-tutorial/

https://s3.amazonaws.com/sparksummit-share/ml-ams-1.0.1/wiki-w2v/python/wiki-w2v_student.html

** Remove stop words
** Compare two documents
** http://vene.ro/blog/word-movers-distance-in-python.html
** word network
** 词频的图
** pattern machine learning
** Timeline




# important
# https://radimrehurek.com/gensim/models/word2vec.html
wmdistance(document1, document2)
Compute the Word Mover’s Distance between two documents. When using this code, please consider citing the following papers:

Note that if one of the documents have no words that exist in the Word2Vec vocab, float(‘inf’) (i.e. infinity) will be returned.

This method only works if pyemd is installed (can be installed via pip, but requires a C compiler).

Example:
test


It is not always a good solution to remove the stop words, sometime this action may influence the logic of the sentence.




Tasks:
 1. I am very interested in the evolution of the term "comprehensive risk management."

 2. I suggested making a figure that shows the timeline of similarity scores (SS) between some of the key terms. For example, we would expect the SS of "loss" and "insurance" to increase over time (as well as "damage" and "insurance"). Likewise, we would expect the SS of "loss" and "compensation" to decrease over time.   In the same vein, words like "risk" probably were less related to our insurance industry terms at the beginning of the UNFCCC.
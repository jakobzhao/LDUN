# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University


from tika import parser
import os
import sys
# from gensim.models import Word2Vec
from pymongo import MongoClient, errors
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords


def review_to_wordlist(review, remove_stopwords=False):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(review, 'html5lib').get_text()
    #
    # 2. Remove non-letters
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    #
    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    #
    # 4. Optionally remove stop words (false by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    #
    # 5. Return a list of words
    return(words)

# Download the punkt tokenizer for sentence splitting
import nltk.data

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


# Define a function to split a review into parsed sentences
def review_to_sentences(review, tokenizer, remove_stopwords=False):
    # Function to split a review into parsed sentences. Returns a
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(review.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            new_sentence = review_to_wordlist(raw_sentence, remove_stopwords)
            if new_sentence != []:
                sentences.append(new_sentence)
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences

# database connection
client = MongoClient("localhost", 27017)
db = client["undocs"]

search_json = {}
docs = db.docs.find(search_json)
count = docs.count()
print count
i = 0
frequency = {}
for doc in docs:
    i += 1
    # print i
    sentences = doc[u'sentences']
    for sentence in sentences:
        for word in sentence:
            if word != u"none":
                count = frequency.get(word, 0)
                frequency[word] = count + 1
frequency_list = frequency.keys()
# for words in frequency_list:
#     print words, frequency[words]

a = open("text.txt", "w")

for item in sorted(frequency, key=frequency.__getitem__, reverse=True):
    text = "%s,%d\n" % (item, frequency[item])
    a.write(text)
print "completed!"




# sentences = review_to_sentences(total, tokenizer)
#
# model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=16)
# model.save("a-1201.w2v")



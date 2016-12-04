# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University


from pymongo import MongoClient
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
# Download the punkt tokenizer for sentence splitting
import nltk.data

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# Download the punkt tokenizer for sentence splitting
import nltk.data

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


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
            if new_sentence != [] and new_sentence != [u'none']:
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
for doc in docs:
    i += 1
    content = doc[u'content']
    sentences = review_to_sentences(content, tokenizer)
    print sentences
    try:
        db.docs.update({'_id': doc[u'_id']}, {'$set': {'sentences_keep_swords': sentences}})
        print "========================"
    except:
        print "error"
        pass
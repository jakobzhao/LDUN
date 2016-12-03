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

# update the encoding system
reload(sys)
sys.setdefaultencoding('utf-8')

# reading all the file names
filenames = []
list_dirs = os.walk("Documents")
for root, dirs, files in list_dirs:
    for d in dirs:
        # print os.path.join(root, d)
        filenames.append(os.path.join(root, d))
    for f in files:
        # print os.path.join(root, f)
        filenames.append(os.path.join(root, f))

# processing the names
content, tier, year, num = "", 0, 0, 0


client = MongoClient("localhost", 27017)
db = client["undocs"]

for filename in filenames:
    if filename[-3:] == "pdf":
        # content
        text = parser.from_file(filename)['content']
        try:
            content = unicode(text)
            # content = ""
        except:
            content = ""
        # Tier 1
        if u"Tier_1" in filename:
            tier = 1
            tags_string = filename.split("\\")[-2]
            tags = tags_string.split("_")
            year = tags[0]
            type = tags[1]
            if len(tags) == 3:
                num = 0
            else:
                num = float(tags[2])
        # Tier 2
        elif u"Tier_2" in filename:
            tier = 2
            tags_string = filename.split("\\")[-2]
            tags = tags_string.split("_")
            year = tags[0]
            type = tags[1]
            num = float(tags[2])
        # Tier 3
        else:
            tier = 3
            tags_string = filename.split("\\")[-2]
            tags = tags_string.split("_")
            year = tags[0]
            type = tags[1]
            num = float(tags[2])

        item_json = {
            'tier':     tier,
            'year':     year,
            'num':      num,
            'filepath': root,
            'filename':  filename.split("\\")[-1],
            'content':  content,
        }
        print item_json

        try:
            db.docs.insert_one(item_json)
        except errors.DuplicateKeyError:
            print "this item may have already been inserted."

#
# from bs4 import BeautifulSoup
# import re
# from nltk.corpus import stopwords
#
#
# def review_to_wordlist(review, remove_stopwords=False):
#     # Function to convert a document to a sequence of words,
#     # optionally removing stop words.  Returns a list of words.
#     #
#     # 1. Remove HTML
#     review_text = BeautifulSoup(review).get_text()
#     #
#     # 2. Remove non-letters
#     review_text = re.sub("[^a-zA-Z]"," ", review_text)
#     #
#     # 3. Convert words to lower case and split them
#     words = review_text.lower().split()
#     #
#     # 4. Optionally remove stop words (false by default)
#     if remove_stopwords:
#         stops = set(stopwords.words("english"))
#         words = [w for w in words if not w in stops]
#     #
#     # 5. Return a list of words
#     return(words)
#
# # Download the punkt tokenizer for sentence splitting
# import nltk.data
#
# # Load the punkt tokenizer
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#
#
# # Define a function to split a review into parsed sentences
# def review_to_sentences(review, tokenizer, remove_stopwords=False ):
#     # Function to split a review into parsed sentences. Returns a
#     # list of sentences, where each sentence is a list of words
#     #
#     # 1. Use the NLTK tokenizer to split the paragraph into sentences
#     raw_sentences = tokenizer.tokenize(review.strip())
#     #
#     # 2. Loop over each sentence
#     sentences = []
#     for raw_sentence in raw_sentences:
#         # If a sentence is empty, skip it
#         if len(raw_sentence) > 0:
#             # Otherwise, call review_to_wordlist to get a list of words
#             sentences.append(review_to_wordlist(raw_sentence, remove_stopwords))
#     #
#     # Return the list of sentences (each sentence is a list of words,
#     # so this returns a list of lists
#     return sentences
#
#
# sentences = review_to_sentences(total, tokenizer)
#
# model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=16)
# model.save("a-1201.w2v")
#
#

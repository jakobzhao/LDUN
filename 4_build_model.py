# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University


import sys
from pymongo import MongoClient
from gensim.models import Word2Vec, Phrases

# update the encoding system
reload(sys)
sys.setdefaultencoding('utf-8')


client = MongoClient("localhost", 27017)
db = client["undocs"]

search_json = {}
docs = db.docs.find(search_json)
count = docs.count()
print count
i = 0
all_sentences = []
for doc in docs:
    i += 1
    print i
    sentences = doc[u'sentences']
    all_sentences += sentences

bigram_transformer = Phrases(all_sentences)

# print list(bigram_transformer[all_sentences])



###########################################################################
# a = open("phrase.csv", "w")
# frequency = bigram_transformer.vocab
# for item in sorted(frequency, key=frequency.__getitem__, reverse=True):
#     text = "%s,%d\n" % (item, frequency[item])
#     a.write(text)
# print "completed!"
# exit(0)
#############################################################################

# model = Word2Vec(bigram_transformer[all_sentences], size=100, window=10, min_count=5, workers=16)
model = Word2Vec(all_sentences, size=100, window=10, min_count=5, workers=16)
model.save("all_words_1202.w2v")
print "completed!"

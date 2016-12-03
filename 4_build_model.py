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
from gensim.models import Word2Vec

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

model = Word2Vec(all_sentences, size=100, window=10, min_count=5, workers=16)
model.save("all_1202.w2v")
print "completed!"

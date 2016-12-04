# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University

from gensim.models import Word2Vec

from tika import parser
import os
import sys
from pymongo import MongoClient, errors

# update the encoding system
reload(sys)
sys.setdefaultencoding('utf-8')


model = Word2Vec.load("all_phrases_1202.w2v")
# model = Word2Vec.load("all_words_1202.w2v")

print model.similarity('damage', 'compensation')
print model.similarity('loss', 'compensation')
print model.similarity('insurance', 'compensation')
# print model.similarity('climate', 'climatic')
# print model.similarity('insurance', 'climate')
# print model.similarity('have', 'we')


# print model.most_similar('climate change')

print "model.most_similar('resilience')"
print model.most_similar('resilience', topn=20)

print "model.most_similar('viable')"
print model.most_similar('viable', topn=20)

print "model.most_similar('cooke')"
print model.most_similar('cooke', topn=20)

print "model.most_similar('munich')"
print model.most_similar('munich')

print "model.most_similar('swiss')"
print model.most_similar('swiss')

print "model.most_similar('insurance')"
print model.most_similar('insurance')

print "model.most_similar('reinsurance')"
print model.most_similar('reinsurance')

print "model.most_similar('compensation')"
print model.most_similar('compensation', topn=20)
#
# print "model.most_similar('re')"
# print model.most_similar('re', topn=30)

print "model.most_similar('risk')"
print model.most_similar('risk')

print "model.most_similar('loss')"
print model.most_similar('loss')


print "model.most_similar('damage')"
print model.most_similar('damage')

print "model.most_similar('vulnerability')"
print model.most_similar('vulnerability')


print "model.most_similar('liability')"
print model.most_similar('liability')

print "model.most_similar('climate')"
print model.most_similar('climate')

print "model.most_similar('finance')"
print model.most_similar('finance')




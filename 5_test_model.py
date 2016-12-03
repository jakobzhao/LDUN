# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University

from gensim.models import Word2Vec


model = Word2Vec.load("all_1202.w2v")

# print model.similarity('global', 'world')
# print model.similarity('climate', 'climatic')
# print model.similarity('insurance', 'climate')
# print model.similarity('have', 'we')

print "model.most_similar('insurance')"
print model.most_similar('insurance', topn=20)

print "model.most_similar('re')"
print model.most_similar('re', topn=30)

print "model.most_similar('reinsurance')"
print model.most_similar('reinsurance', topn=20)

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

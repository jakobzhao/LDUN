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

a = open("word_insurance_time_series_new.csv", "w")
a.write("year, damage, loss\n")

for year in range(1995, 2017):
    model = Word2Vec.load("model/words/words_year_%s_1203.w2v" % year)
    try:
        damage = model.similarity('damage', 'insurance')
        print damage
    except:
        damage = 0.1
    try:
        loss = model.similarity('loss', 'insurance')
        print loss
    except:
        loss = 0.1
    # try:
    #     insurance = model.similarity('insurance', 'climate')
    #     print insurance
    # except:
    #     insurance = 0.1
    a.write("%s,%s,%s\n" % (year, damage, loss))
a.close()
print "completed!"

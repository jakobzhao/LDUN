# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University

from gensim.models import Word2Vec

import os
import sys
from pymongo import MongoClient, errors

# update the encoding system
reload(sys)
sys.setdefaultencoding('utf-8')

# a = open("word_insurance_time_series.csv", "w")
# a.write("year, damage, loss\n")

for year in range(1995, 2017):
    # model = Word2Vec.load("model/phrases/phrases_year_%s_1203.w2v" % year)
    model = Word2Vec.load("model/words/words_year_%d_1203.w2v" % year)
    try:
        print model.most_similar('risk management')
        # print str(year) + ": " + str(model.most_similar('reinsurance', topn=5))
    except:
        print "============"

    # a.write("%s,%s,%s\n" % (year, damage, loss))
# a.close()
print "completed!"

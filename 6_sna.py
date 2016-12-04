# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Nov 24, 2016
# @author:       Bo Zhao
# @email:        zhao2@oregonstate.edu
# @website:      https://github.com/jakobzhao/
# @organization: College of Earth, Ocean, and Atmospheric Sciences, Oregon State University

import networkx as nx
from gensim.models import Word2Vec


def generate_sematic_network3(keyword, related_keywords, threshold=0.5, depth=10, w2v_file='', gexf_file=''):
    model = Word2Vec.load(w2v_file)
    g = nx.DiGraph()
    g.add_node(keyword)
    for related in related_keywords:
        g.add_node(related)
        w = model.similarity(keyword, related)
        g.add_edge(related, keyword, weight=int(w * w * 100 / threshold / threshold))
        print keyword, related, w

    # for related_1 in related_keywords:
    #     for related_2 in related_keywords:
    #         if related_1 != related_2:
    #             p = model.similarity(related_1, related_2)
    #             g.add_edge(related_2, related_1, weight=int(p*p*100))
    #             print related_1, related_2, w

    for related in related_keywords:
        g.add_node(related)
        for w, i in model.most_similar(related, topn=depth):
            if i > threshold:
                g.add_node(w)
                g.add_edge(w, related, weight=int(i * i * 100))
                notice = (w + ' ' + str(i)).encode('gbk', 'ignore')
                print notice
                for t, j in model.most_similar(w, topn=depth):
                    if j > threshold:
                        g.add_node(t)
                        g.add_edge(t, w, weight=int(j * j * 100))
                        notice = (t + ' ' + str(j)).encode('gbk', 'ignore')
                        print notice
    # notice = (s + ' ' + str(k)).encode('gbk', 'ignore')
    # log(NOTICE, notice)
    nx.write_gexf(g, gexf_file, prettyprint=True)
    print "complete"


generate_sematic_network3("climate", ("adaption", "risk", "loss", "damage", "insurance"),0.5, 10, "all_words_1202.w2v", "climate.gexf")
if __name__ == '__main__':
    pass

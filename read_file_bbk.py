#!/usr/bin/env python
# -*- coding: utf8 -*-
from os import listdir
from collections import defaultdict

def read_file(filename):
    infile = open(filename,'r')

    contents = infile.readlines()
    infile.close()
    return contents


def list_textfiles(directory):
    textfiles = []

    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)

    return textfiles

def list_bbk(texts):
    bbk_words = []
    bbk = dict()

    n = len(texts)
    for i in xrange(0,n):
        for j in xrange(0,len(texts[i])):

            for line in texts[i][j].split("	"):
                bbk_words.append(line)
            #print bbk_words
            bbk[bbk_words[0]] = bbk_words[1]
            bbk_words = []


    return bbk



path = list_textfiles("/Users/elena/Documents/BBK")

for filepath in path:
    texts = []
    texts.append(read_file(filepath))

print list_bbk(texts).keys()
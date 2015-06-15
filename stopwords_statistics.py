# -*- coding: utf-8 -*-
import hashlib
import numpy as np
from read_files import read_file, list_textfiles_files
from nltk.corpus import stopwords
from bbk_matrix import matrix
path = list_textfiles_files('/Users/elena/Documents/BBK_materials/AUTOREF/TXT')

all_bbk_texts = [read_file(filepath[0]) for filepath in path]

stopwords_russian = stopwords.words('russian')

t, v, p = matrix(all_bbk_texts,stopwords_russian)

vocab_doc = {}
for tag, count in zip(v,p):
    vocab_doc[tag] = count


for w in p:
    print w
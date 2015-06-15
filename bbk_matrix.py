# -*- coding: utf-8 -*-
import hashlib
import numpy as np
from read_files import read_file, list_textfiles

from sklearn.feature_extraction.text import CountVectorizer

unique_words = []
with open('unique_words.txt','r') as f:
    unique_words = f.readlines()

for word in unique_words:
    word = word.strip()

path_clean_text = list_textfiles('/Users/elena/PycharmProjects/bbk_classification/autoref_clean/')
all_clean_texts = [read_file(filepath) for filepath in path_clean_text]
#print all_clean_texts[0]
unique_words_bbk = []
words_bbk = []
with open('unique_words_bbk_cleaned.txt','r') as f:
    unique_words_bbk = f.readlines()
    for word in unique_words_bbk:
        word = word.rstrip()
        words_bbk.append(word.decode('utf-8'))


#print words_bbk[0:10]
def bbk_dict(doc):
    bbk = {}
    i = 0
    for word in doc:
        bbk[word.strip()] = i
        i += 1
    return bbk

print bbk_dict(words_bbk).items()[0:10]

def matrix(all_clean_texts,vocab=None):
    vectorizer = CountVectorizer(analyzer = "word", input="content",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 10000, vocabulary=vocab)
    train_data_features = vectorizer.fit_transform(all_clean_texts)
    train_data_features = train_data_features.toarray()
    print train_data_features.shape
    vocab = vectorizer.get_feature_names()
    dist = np.sum(train_data_features, axis=0)
    return train_data_features, vocab, dist

t, v, p = matrix(all_clean_texts,words_bbk)
#t, v, p = matrix(all_clean_texts)#,bbk_dict(unique_words))
vocab_doc = {}
for tag, count in zip(v,p):
    vocab_doc[tag] = count

vocab_doc = sorted(vocab_doc.items(), key=lambda x: x[1], reverse=True)
#vocab_doc = vocab_doc.items()


with open('freq_words_bbk.txt','w') as f:
    for (key, value) in vocab_doc:
        f.write(key.encode('utf-8') + '\t' + str(value) + '\n')

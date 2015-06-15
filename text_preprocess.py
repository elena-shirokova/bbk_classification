# -*- coding: utf8 -*-
from pymorphy import *
from nltk import *
from nltk.corpus import stopwords
import re
import string
from read_files import read_file, list_textfiles, list_textfiles_files
morph=get_morph('/Users/elena/Downloads/ru.sqlite-json')

def tokenize_text(raw_docs):
    tokenized_docs = [word_tokenize(doc.decode('utf-8').upper()) for doc in raw_docs]

    return tokenized_docs

def remove_punct(path):
    regex_punct = re.compile('[%s]' % re.escape(string.punctuation))
    regex_digits = re.compile('[%s]' % re.escape(string.digits))
    tokenized_docs_no_punctuation = []
    #all_bbk_texts = []#[read_file(filepath[0]) for filepath in path]

    for filepath in path:

        doc = read_file(filepath[0])
        tokenized_doc = word_tokenize(doc.decode('utf-8').upper())
        #for review in tokenized_docs:
        filename = '/Users/elena/PycharmProjects/bbk_classification/autoref_clean/' + str(filepath[1])
        f = open(filename,'a')
        new_review = []
        for token in tokenized_doc:
            token = token.replace(u'ё',u'е')
            new_token = regex_punct.sub(u'', token)
            new_token = regex_digits.sub(u'', new_token)

            if not new_token == u'':
                if not new_token in stopwords.words('russian'):
                    if len(new_token) > 5:
                        norm_form = morph.normalize(new_token)
                        if type(norm_form) == set:

                            norm_word = norm_form.pop().lower()
                            new_review.append(norm_word)
                            f.write(norm_word.encode('utf-8') + '\n')
                        else:
                            new_review.append(norm_word)
                            f.write(norm_word.encode('utf-8') + '\n')

        tokenized_docs_no_punctuation.append(new_review)
    return tokenized_docs_no_punctuation

def bag_of_words(list_of_all_words):
     print "start"
#makes unique list of words from all words in the list of lists
     set_of_unique_words = []
     for doc in list_of_all_words:
          print list_of_all_words.index(doc)
          set_of_unique_words += doc
          #print set_of_unique_words.index(doc)
     return list(set(set_of_unique_words))


path = list_textfiles_files('/Users/elena/Documents/BBK_materials/AUTOREF/TXT')

#all_bbk_texts = [read_file(filepath[0]) for filepath in path]
texts = remove_punct(path)

"""text_clean = normalize_words(remove_stopwords(texts))

bag_of_unique_words =  bag_of_words(text_clean)

with open('unique_words.txt','a') as f:
    for word in bag_of_unique_words:
        f.write(word.encode('utf-8') + '\n')
print len(bag_of_unique_words)"""
__author__ = 'elena'
from text_preprocess import *

path = list_textfiles('/Users/elena/Documents/BBK_materials/AUTOREF/TXT')

all_bbk_texts = [read_file(filepath) for filepath in path]
texts = remove_punct(tokenize_text(all_bbk_texts[0:]))

text_clean = normalize_words(remove_short(remove_stopwords(texts)))

bag_of_unique_words =  bag_of_words(text_clean)

with open('unique_words.txt','a') as f:
    for word in bag_of_unique_words:
        f.write(word.encode('utf-8') + '\n')
print len(bag_of_unique_words)
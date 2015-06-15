# -*- coding: UTF-8 -*-
from pylab import *
import matplotlib.pyplot as p
import pandas as pd
from read_file_bbk import list_textfiles
from collections import Counter
from plots import bar_plot

font = {'family': 'Verdana',
        'weight': 'normal'}
rc('font', **font)

letters = ["Г","Н","П","С","Т","У","А","Б","В","Е","Ж","З","И","К","Л","М","О","Ф","Х"]
count_letters = [2623,2428,7073,1283,9390,8872,1013,97,9146,5972,882,4409,986,2677,2422,1508,2731,2549,3653]
letters_id = [i+1 for i in xrange(0,len(count_letters))]
#p.bar(letters,count_letters)
#p.xlabel(u'Буквы')
#p.ylabel(u'Количество')
#p.title(u'Количество классов в ББК по буквам')
#p.show()

all_paths = list_textfiles("/Users/elena/Documents/BBK/matrix_bbk_by_row")




def read_from_files(all_paths):
    bbk_rows = []
    for path in all_paths:
        print path
        data = [int(line.strip()) for line in open(path,'r')]
        bbk_rows.append(data)
        return bbk_rows


filename = '/Users/elena/Documents/BBK/unique_words_bbk.txt'

bbk_words_unique = [line.strip() for line in open(filename,'r')]



#D = Counter(bbk_rows[0])

#words_id = [i for i in xrange(0,len(bbk_rows[1]))]

#bar_plot(words_id,bbk_rows[2],u'Номер слова', u'Частота слова', u'Распределение слов в ББК по букве В')








import glob, os

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, titlePattern % title + ext))


#rename(r'/Users/elena/Documents/BBK_materials/words_freq_autoref', r'*', r'%s.txt')

path_autoref_freq = list_textfiles('/Users/elena/Documents/BBK_materials/words_freq_autoref')

autoref_rows = []
for path in path_autoref_freq:
    data = [int(line.strip()) for line in open(path,'r')]
    autoref_rows.append(data)


count_non_zero_words = []
for elements in autoref_rows:
    count_non_zero_words.append(sum(x > 0 for x in elements))


id_autoref = [i for i in xrange(0, len(autoref_rows))]

#bar_plot(id_autoref,count_non_zero_words,u'Номер автореферата', u'Количество ненулевых слов', u'Количество слов с ненулевой частотой в авторефератах')

#print count_non_zero_words.index(min(count_non_zero_words)), min(count_non_zero_words)


word_id_autoref = [i for i in xrange(0, len(autoref_rows[35]))]

for i in xrange(0,len(autoref_rows[])):
    if autoref_rows[994][i] > 0:
        #print 'index',i
        print 'word', bbk_words_unique[i]


#print bbk_words_unique[8018]

#bar_plot(word_id_autoref,autoref_rows[35],u'Номер слова', u'Частота слова', u'Распределение слов в ББК по автореферату 994')
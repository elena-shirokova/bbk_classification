#! /usr/local/bin/python
# -*- coding: utf8 -*-
from os import listdir
from tree_bbk import Tree
from pygraphviz import *
import pickle
import macholib as plt

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

def split_str(text):

    for elements in text:

        if elements == " ":

            return text.split(" ")

        elif elements == "	":

            return text.split("	")

        elif elements == "   ":

            return text.split("   ")

        elif elements == "	":

            return text.split("	")


def list_bbk(texts):
    bbk_words = []
    bbk = []

    n = len(texts)

    for i in xrange(0,len(texts)):

        for j in xrange(1,len(texts[i])):

            line = split_str(texts[i][j])
            bbk_words.append(line)

            bbk.append(bbk_words)

            bbk_words = []



    return bbk





def count_delim(node,element):

    if  (element.count(" -- ") - node.count(" -- ")) == 1:
        return True
    else:
        return False


def find_substr(node,element):

    if (node != element) and (element.find(node) != -1):
        return True
    else:
        False


def find_children(node,texts):

    children = []

    for i in xrange(0,len(texts)):


        for j in xrange(0,len(texts[i])):

            if count_delim(node,(split_str(texts[i][j])[1].strip())) == True and find_substr(node,(split_str(texts[i][j])[1].strip())) == True:

                child = (split_str(texts[i][j])[0].strip())

                children.append(child)

    return children


def all_child(texts):

    all_children = []

    for i in xrange(0,len(texts)):

        for j in xrange(1,len(texts[i])):

            local_children = find_children(split_str(texts[i][j])[1].strip(),texts)

            for child in local_children:

                all_children.append(child)

    return all_children


def create_tree(texts):

    tree = []

    children = []

    all_children = all_child(texts)

    #tree.append((split_str(texts[0])[0].strip(),split_str(texts[0])[0].strip()))

    for i in xrange(0,len(texts)):

        for j in xrange(0,15):

            if split_str(texts[i][j])[1].strip() not in all_children:

                children = find_children(split_str(texts[i][j])[1].strip(),texts)

                for child in children:

                    tree.append((split_str(texts[i][j])[0].strip(),child))


    return tree

path = list_textfiles("/Users/elena/Documents/BBK")


texts = [read_file(filepath) for filepath in path]

result = create_tree(texts)
print len(texts)


bbk_words = []

for i in xrange(0, len(texts)):
    for j in xrange(0,len(texts[i])):
        bbk_words.append(split_str(texts[i][j])[1])


bbk_final = []
split_bbk = []
for bbk_word in bbk_words:


    if " -- " not in bbk_word:
        bbk_final.append(bbk_word)

    elif " -- " in bbk_word:

        split_bbk = bbk_word.split(" -- ")

        bbk_words.remove(bbk_word)

        for elem in split_bbk:
            bbk_final.append(elem)

print bbk_final[19]
print len(bbk_final)

def getUniqueWords(allWords) :
    uniqueWords = []
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords

f = open('/Users/elena/Desktop/bbk.txt','w')

for sentence in bbk_final:
    f.write(sentence + '\n')
f.close()


t = Tree()
for i in result:t.push(i)


G = AGraph()


for i in xrange(0,len(result)):
    G.add_edge(result[i][0].decode('utf8'), result[i][1].decode('utf8'),color='plum', style='filled', shape='box')

G.layout(prog='dot')
G.draw('file.png')




letters = ['Г', "Н","П","С","Т","У","А","Б","В","Е","Ж","З","И","К","Л","М","О","Ф","Х"]
count_letters = [2623,2428,7073,1283,9390,8872,1013,97,9146,5972,882,4409,986,2677,2422,1508,2731,2549,3653]



#plt.plot(letters,count_letters)
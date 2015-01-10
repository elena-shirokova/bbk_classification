#! /usr/local/bin/python
# -*- coding: utf8 -*-
from os import listdir


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


path = list_textfiles("/Users/elena/Documents/BBK")

texts = [read_file(filepath) for filepath in path]


a = split_str(texts[0][0])[1].strip()
b = split_str(texts[0][2])[1].strip()

t = Tree()
for i in result:t.push(i)

for node in t.roots: node.print_()
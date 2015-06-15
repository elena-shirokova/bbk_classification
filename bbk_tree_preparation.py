#! /usr/local/bin/python
# -*- coding: utf8 -*-
from read_file_bbk import split_str


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

    for j in xrange(0,len(texts)):

        if count_delim(node,(split_str(texts[j])[1].strip())) == True and find_substr(node,(split_str(texts[j])[1].strip())) == True:

            child = (split_str(texts[j])[0].strip())

            children.append(child)

    return children


def all_child(texts):

    all_children = []

    local_children =[]

    for j in xrange(1,len(texts)):

        local_children = find_children(split_str(texts[j])[1].strip(),texts)

        for child in local_children:

            all_children.append(child)

    return all_children


def create_tree(texts):

    tree = []

    children = []

    all_children = all_child(texts)

    tree.append((split_str(texts[0])[0].strip(),split_str(texts[0])[0].strip()))

    for j in xrange(1,len(texts)):

        if split_str(texts[j])[1].strip() not in all_children:

            children = find_children(split_str(texts[j])[1].strip(),texts)

            for child in children:

                tree.append((child,split_str(texts[j])[0].strip()))


    return tree
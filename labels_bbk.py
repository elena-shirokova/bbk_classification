# -*- coding: utf-8 -*-
import re

from read_files import read_file, list_textfiles_label
from sklearn.preprocessing import LabelEncoder
label_path = '/Users/elena/Documents/BBK_materials/AUTOREF/MRC'

textfiles = list_textfiles_label(label_path)

def label_encode(textfiles):
    le = LabelEncoder()
    label_list = []
    for pair in textfiles:
        labels = []
        rubbk_label = read_file(pair[0]).split()

        for word in rubbk_label:
            if '2rubbk' in word:
                lbl = word.split(',')[0]

                label_list.append(lbl.decode('utf-8')[2:3])
    le.fit(label_list)
    code_list = le.transform(label_list)
    inverse_list = le.inverse_transform(code_list)

    for_dict = zip(code_list,inverse_list)
    label_code_dict = {}
    for pair in for_dict:
        label_code_dict[pair[1]] = pair[0]
    return label_code_dict


label_code =  label_encode(textfiles)
#print label_code.items()[1][1]


def get_labels(textfiles):
    label_dict = {}
    labels = []
    p = r"[А-Я0-9]{2}"
    pattern = re.compile(p)
    for pair in textfiles:
        lbls = []
        rubbk_label = read_file(pair[0]).split()

        for word in rubbk_label:
            word = word.strip()
            if 'rubbk' in word:
                if ',' in word or ')' in word:


                    print word
                    lbl = word.split(',')[0]
                    lbls.append(lbl.decode('utf-8')[2:3])

        labels.append(lbls)
        label_dict[pair[1].split('.')[0]] = lbls


    return label_dict

print get_labels(textfiles)
bbk_lbl =  get_labels(textfiles)
"""for x,y in bbk_lbl.items():
    if len(y) == 0:
        print x"""
print len(bbk_lbl)
length = [len(bbk) for bbk in bbk_lbl]
print min(length)
print max(length)

"""f = open('y.full_bbk_1st_letter.csv', 'a')

for i,result in bbk_lbl.items():

    if len(result)  == 1 :
        print >> f, str(i) + ',' + str(result[0].encode('utf-8'))
    elif len(result)  == 2:
        print >> f, str(i) + ',' + str(result[0].encode('utf-8')) + ',' + str(result[1].encode('utf-8'))
    elif len(result)  == 3:
        print >> f, str(i) + ',' + str(result[0].encode('utf-8')) + ',' + str(result[1].encode('utf-8')) + ',' + str(result[2].encode('utf-8'))
    elif len(result)  == 4:
        print >> f, str(i) + ',' + str(result[0].encode('utf-8')) + ','\
                    + str(result[1].encode('utf-8')) + ',' + str(result[2].encode('utf-8')) + ',' + str(result[3].encode('utf-8'))


f.close()"""


f = open('y_all_labels_code.csv', 'w')
#print >> f, 'file,BBK_label'
for result in bbk_lbl:
    if len(result) == 0:
        print >> f, str(0)
    elif len(result)  == 1:
        #print >> f, str(i) + ',' + str(result[0].encode('utf-8'))
        print >> f, str(label_code[result[0]])
    elif len(result)  == 2:
        print >> f, str(label_code[result[0]]) + ',' + str(label_code[result[1]])
    elif len(result)  == 3:
        print >> f,  str(label_code[result[0]]) + ',' + str(label_code[result[1]])\
                     + ',' + str(label_code[result[0]])
    elif len(result)  == 4:
        print >> f, str(label_code[result[0]]) + ',' + str(label_code[result[1]])\
                    + ',' + str(label_code[result[2]]) + ',' + str(label_code[result[3]])
f.close()
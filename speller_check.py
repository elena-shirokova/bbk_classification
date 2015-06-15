# -*- coding: utf-8 -*-
import requests
from subprocess import Popen, PIPE
import re
import string
def check_speller(list_of_words):

    params = dict()
    params['LANG'] = 'ru'

    for idx,item in enumerate(list_of_words):

        params['text'] = list_of_words[idx]

        i = 1


        #proxy = ["82.117.234.20"]
        #proxies = {"http": "http://" + proxy[i-1]}
        r = requests.get('http://speller.yandex.net/services/spellservice.json/checkText')

        if r.json() == []:

            list_of_words[idx] = list_of_words[idx]

        elif r.json()[0]['s'] != []:

            list_of_words[idx] = r.json()[0]['s'][0]



        elif r.json()[0]['s'] == []:

            try:

                list_of_words.remove(list_of_words[idx])

            except ValueError:

                pass
    return list_of_words


unique_words = []
with open('unique_words.txt','r') as f:
    unique_words = f.readlines()

for word in unique_words:
    word = word.strip()
list_of_words_test = ['леин','арел','велосепед', 'провет','мой']

regex_punct = re.compile('[%s]' % re.escape(string.punctuation))
new_review = []
for word in unique_words:
    new_token = regex_punct.sub(u'', word)

    if not new_token == u'':
        new_review.append(new_token.strip())


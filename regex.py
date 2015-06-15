# -*- coding: utf-8 -*-
import re

p = r"[А-Я0-9]{2}"
pattern = re.compile(p)
text = 'aА511.1,02rubbk'
print pattern.match(text[2:5])
print text[2:5]


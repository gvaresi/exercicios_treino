# -*- coding: utf-8 -*-
"""
Use for, split() e if para criar uma declaração que imprima as palavras que começam com 's':
"""


st = 'Print only the words that start with s in this sentence'

for s in st.split():
    if s[0][0] == 's':
        print(s)

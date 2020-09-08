# -*- coding: utf-8 -*-
"""
Use Compreensão em listas para criar uma lista das primeiras letras de cada palavra na string abaixo:
"""


st3 = 'Create a list of the first letters of every word in this string'
palavras = st3.split()

for primeira_palavra in st3.split():
    print(primeira_palavra[0])

letra = [letra[0] for letra in palavras]

print(letra)

"""Escreva uma função Python para verificar se uma string é um pangrama ou não.

     Nota: Pangramas são palavras ou frases contendo cada letra do alfabeto pelo menos uma vez.

Dica: veja o módulo de strings
"""

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    num = len(alphabet)
    cont = 0

    for i in alphabet:
        if i in str1:
            cont += 1

    return print(num == cont)


ispangram("The quick brown fox jumps over the lazy dog")

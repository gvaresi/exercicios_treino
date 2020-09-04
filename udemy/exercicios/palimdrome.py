"""
** Escreva uma função Python que verifica se uma string passada é palindrome ou não. **

Nota: Um palíndromo é palavra, frase ou seqüência que lê o mesmo para trás.
"""


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


palindrome('helleh')

"""
** Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas. **

 Exemplo de Cadeia: 'Olá Sr. Rogers, como você está bem, terça-feira?'
 Saída esperada:
 Número de caracteres maiúsculas: 3
 Número de caracteres minúsculos: 33

Se você se sentir ambicioso, explore o módulo de Coleções para resolver esse problema!
"""


texto_return = """
Voce tem {0} caracteres maiusculos
voce tem {1} caracter minusculos
"""

texto = 'Olá Sr. Rogers, como você está bem, terça-feira?'


def up_low(s):
    up = 0
    low = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    return print(texto_return.format(up, low))


up_low(texto)

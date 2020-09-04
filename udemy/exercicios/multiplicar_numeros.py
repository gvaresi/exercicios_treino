"""
** Escreva uma função Python para multiplicar todos os números em uma lista. **

     Lista de exemplos: [1, 2, 3, -4]      Saída esperada: -24
"""


def multiply(*numbers):
    aux = 1
    for x in numbers:
        aux *= x
    return print(aux)


multiply(1, 2, 3, -4)

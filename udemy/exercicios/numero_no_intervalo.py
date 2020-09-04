"""
Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)
"""


num = int(input('Informe um numero: '))
low = 5
high = 200


def ran_check(num, low, high):
    if num in list(range(low, high + 1)):
        return print('Verdadeiro, o numero esta no intervado de ', low, high)
    else:
        return print('Falso, o numero não esta no intervado de ', low, high)


ran_check(num, low, high)

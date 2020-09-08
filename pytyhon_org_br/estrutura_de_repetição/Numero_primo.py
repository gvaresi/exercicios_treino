"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""


num_1 = int(input('Informe um numero: '))

primo = 'O numero {0} é primo.'
nao_primo = 'O numero {0} não é primo.'

if num_1 == 1 or num_1 == 2:
    print(primo.format(num_1))


def numero(n: int):
    for x in range(2, n + 1):
        if num_1 % x == 0:
            if x == num_1:
                return print(primo.format(num_1))
            else:
                return print(nao_primo.format(num_1))


numero(num_1)

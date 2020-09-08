"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

Altere Wo programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""


num_1 = int(input('Informe um numero: '))
primo = 'O numero {0} é primo porque ele é so  divisivel pelos seguintes numeros {1}.'
nao_primo = 'O numero {0} não é primo porque ele é divisivel pelos seguintes numeros {1}.'

if num_1 == 1 or num_1 == 2:
    print(primo.format(num_1))


def numero(n: int):
    div_primo = [1]
    for x in range(2, n + 1):
        if num_1 % x == 0:
            if x == num_1:
                div_primo.append(x)
                return print(primo.format(num_1, div_primo))
            else:
                for y in range(2, n + 1):
                    if num_1 % y == 0:
                        div_primo.append(y)
                        if y == num_1:
                            return print(nao_primo.format(num_1, div_primo))


numero(num_1)

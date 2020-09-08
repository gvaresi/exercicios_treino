"""
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.
"""

num_1 = int(input('Digite um numero inteiro: '))
num_2 = int(input('Digite um numero inteiro: '))

soma = 0


print('intervalo dos numeros:')
while num_1 < num_2 - 1:
    num_1 += 1
    soma += num_1
    print(num_1)


print()
print()
print('A soma dos numeros do intervalo é:', soma)

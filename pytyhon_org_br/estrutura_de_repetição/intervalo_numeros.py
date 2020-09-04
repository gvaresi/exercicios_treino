"""
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num_1 = int(input('Digite um numero inteiro: '))
num_2 = int(input('Digite um numero inteiro: '))

while num_1 < num_2 - 1:
    num_1 += 1
    print(num_1)

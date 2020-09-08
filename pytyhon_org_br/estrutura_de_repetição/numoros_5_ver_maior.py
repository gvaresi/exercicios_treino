"""
Faça um programa que leia 5 números e informe o maior número.
"""

num_1 = int(input('Informe um numero: '))
num_2 = int(input('Informe um numero: '))
num_3 = int(input('Informe um numero: '))
num_4 = int(input('Informe um numero: '))
num_5 = int(input('Informe um numero: '))

maior = num_1
if maior < num_2:
    maior = num_2
if maior < num_3:
    maior = num_3
if maior < num_4:
    maior = num_4
if maior < num_5:
    maior = num_5

print()
print('O maior numero é ', maior)

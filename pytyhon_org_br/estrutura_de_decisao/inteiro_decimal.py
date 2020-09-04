"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""

number = input('informe um numero :')


if type(number) == str:
    print('esse numero é decimal')
else:
    print('Esse numero é inteiro')

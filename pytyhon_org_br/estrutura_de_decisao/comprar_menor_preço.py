"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

preco_1 = float(input('Informe o preço do primeiro produto :'))
preco_2 = float(input('Informe o preço do segundo produto :'))
preco_3 = float(input('Informe o preço do terceiro produto :'))

menor = preco_1

if __name__ == '__main__':
    if menor > preco_2:
        menor = preco_2
    if menor > preco_3:
        menor = preco_3
    if preco_1 == menor:
        print('O Produto qu devemos comprar é o primeiro produto que custa R$', "%.2f" % menor)
    elif menor == preco_2:
        print('O Produto qu devemos comprar é o segundo produto que custa R$', "%.2f" % menor)
    elif preco_3 == menor:
        print('O Produto qu devemos comprar é o terceiro produto que custa R$', "%.2f" % menor)

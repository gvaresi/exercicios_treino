"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""
num_1 = int(input('Digite um numero inteiro:'))
num_2 = int(input('Digite um numero inteiro:'))
num_3 = float(input('Digite um numero real:'))


ope_1 = (num_1 * 2) * (num_2 / 2)
ope_2 = (num_1 * 3) + num_3
ope_3 = num_3 ** 3

if __name__ == '__main__':
    print('o produto do dobro do primeiro com metade do segundo - ', ope_1)
    print('a soma do triplo do primeiro com o terceiro - ', ope_2)
    print('o terceiro elevado ao cubo - ', ope_3)

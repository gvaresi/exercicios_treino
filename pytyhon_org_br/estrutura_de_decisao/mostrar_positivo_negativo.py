"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""


numero_1 = int(input('Digite um numero positivo ou negativo:'))


if __name__ == '__main__':
    if numero_1 >= 0:
        print('O numero digitado é positivo')
    else:
        print('O numero digitado é negativo')

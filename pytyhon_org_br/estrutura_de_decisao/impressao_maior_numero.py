"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
numero_1 = int(input('Digite o primeiro numero:'))
numero_2 = int(input('Digite o segundo numero:'))

if __name__ == '__main__':
    if numero_1 > numero_2:
        print('o maior numero digitado é :', numero_1)
    else:
        print('o maior numero digitado é :', numero_2)

"""
Faça um Programa que leia três números e mostre o maior deles.
"""


maior = int(input('Informe o primeiro numero :'))
numero_2 = int(input('Informe o segundo numero :'))
numero_3 = int(input('Informe o terceiro numero :'))


if __name__ == '__main__':
    if maior < numero_2:
        maior = numero_2
    if maior < numero_3:
        maior = numero_3
    print('o maior numero digitado foi :', maior)

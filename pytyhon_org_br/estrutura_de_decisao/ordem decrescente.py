"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero_1 = int(input('Informe o primeiro numero :'))
numero_2 = int(input('Informe o segundo numero :'))
numero_3 = int(input('Informe o terceiro numero :'))

maior = int(numero_1)
menor = int(numero_1)


if __name__ == '__main__':
    if maior < numero_2:
        maior = numero_2
    if maior < numero_3:
        maior = numero_3
    if menor > numero_2:
        menor = numero_2
    if menor > numero_3:
        menor = numero_3
    if numero_2 < numero_1 < numero_3:
        medio = numero_1
    elif numero_2 > numero_1 > numero_3:
        medio = numero_1
    elif numero_1 < numero_2 < numero_3:
        medio = numero_2
    elif numero_1 > numero_2 > numero_3:
        medio = numero_2
    else:
        medio = numero_3
    print(maior, medio, menor)

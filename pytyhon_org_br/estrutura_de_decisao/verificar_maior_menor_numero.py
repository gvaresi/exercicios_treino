"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
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


print('O maior numero digitado foi :', maior)
print('O menor numero digitado foi :', menor)

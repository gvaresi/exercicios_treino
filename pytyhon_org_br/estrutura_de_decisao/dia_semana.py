"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
numero = int(input('Digite um numero de 1 a 7:'))

while numero < 1 or numero > 7:
    numero = int(input('Digite um numero de 1 a 7:'))

if __name__ == '__main__':
    if numero == 1:
        print('domingo')
    elif numero == 2:
        print('Segunda')
    elif numero == 3:
        print('Terça')
    elif numero == 4:
        print('Quarta')
    elif numero == 5:
        print('Quinta')
    elif numero == 6:
        print('Sexta')
    elif numero == 7:
        print('Sabado')
    else:
        print('Invalido')

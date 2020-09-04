"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

numero = int(input('informe um numero de 0 a 10: '))

while 0 > numero or numero > 10:
    numero = int(input('informe um numero de 0 a 10: '))

print(numero)

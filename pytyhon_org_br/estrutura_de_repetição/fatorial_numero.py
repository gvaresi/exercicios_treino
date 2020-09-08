"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
"""


numero = int(input("informe o numero para exibir o fatorial dele: "))

g = 1
resultado = []

for f in range(numero, 0, -1):
    g *= f
    resultado.append(f)

texto = 'O resultado do fatorial de {0} é {1} = {2}'

print(texto.format(numero, resultado, g))

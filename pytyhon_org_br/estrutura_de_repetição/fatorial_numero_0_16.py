"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""

numero = int(input("informe o numero para exibir o fatorial dele: "))
while 0 >= numero or numero > 16:
    numero = int(input("informe o numero para exibir o fatorial dele: "))
    
numero = 5
g = 1
resultado = []

for f in range(numero, 0, -1):
    g *= f
    resultado.append(f)


texto = 'O resultado do fatorial de {0} é {1} = {2}'    

print(texto.format(numero, resultado, g))

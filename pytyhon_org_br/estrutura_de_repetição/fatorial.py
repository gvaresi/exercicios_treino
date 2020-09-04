"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""

texto_impressao = """ 
                    Fatorial de {0}
                    {0}! = {1} =  {2}
"""
y = 1
lista_numero = []
numero = int(input('Informe um numero inteiro: '))

for x in range(numero, 0, -1):
    lista_numero.append(x)
    y *= x

lista_numero = '.'.join(map(str, lista_numero))

print(texto_impressao.format(numero, lista_numero, y))

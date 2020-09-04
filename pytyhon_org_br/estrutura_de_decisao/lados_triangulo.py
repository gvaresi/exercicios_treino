"""
    Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

lado_1 = input('digite o primeiro lado do triangulo:')
lado_2 = input('digite o segundo lado do triangulo:')
lado_3 = input('digite o terceiro lado do triangulo:')


if __name__ == '__main__':
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Triangulo Equilatero')
    elif lado_3 != lado_2 and lado_3 != lado_1 and lado_1 != lado_2:
        print("Triangulo Escaleno")
    else:
        print('Triangulo Isósceles')

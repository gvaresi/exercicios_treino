"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

numero = int(input("informe um numero :"))

if __name__ == '__main__':
    if (numero % 2) == 0:
        print('o Número ', numero, 'é par')
    else:
        print('o Número ', numero, 'é impar')

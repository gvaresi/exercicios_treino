"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9).
"""

print('Programa para informar a temperatura em Celcius')
farenheit = float(input('Informe a temperatura em Farenheit: '))
celcius = 5 * ((farenheit - 32) / 9)

if __name__ == '__main__':
    print('Atemperatura é de ', celcius, 'G˚ Celcius')

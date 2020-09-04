"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
    C = 5 * ((F-32) / 9).
"""

print('Programa para informar a temperatura em Farenheit')
celcius = float(input('Informe a temperatura em Celcius: '))


farenheit = ((celcius * 9) / 5) + 32

if __name__ == '__main__':
    print('temperatura em Farenheit', farenheit)

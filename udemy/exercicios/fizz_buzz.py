"""
Escreva um programa que imprima os números inteiros de 1 a 100.
Para múltiplos de três imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz".
Para números que são múltiplos de três e cinco imprima "FizzBuzz".
"""

result = []


def fizz_buzz(n: int):
    resultado = []
    for i in range(1, n + 1):
        numero_ou_fizzbuzz = ''
        if i % 3 == 0:
            numero_ou_fizzbuzz = 'fizz'
        if i % 5 == 0:
            numero_ou_fizzbuzz += 'buzz'
        if numero_ou_fizzbuzz == '':
            numero_ou_fizzbuzz = i
        resultado.append(numero_ou_fizzbuzz)
    return print(resultado)


fizz_buzz(1_000)

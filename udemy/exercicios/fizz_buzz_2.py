"""
Escreva um programa que imprima os números inteiros de 1 a 100.
Para múltiplos de três imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz".
Para números que são múltiplos de três e cinco imprima "FizzBuzz".
"""


for fizz_buzz in range(1, 501):
    if fizz_buzz % 5 == 0 and fizz_buzz % 3 == 0:
        print('FizzBuzz')
    elif fizz_buzz % 5 == 0:
        print('Buzz')
    elif fizz_buzz % 3 == 0:
        print('Fizz')
    else:
        print(fizz_buzz)

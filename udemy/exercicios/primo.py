"""
numero primo
"""
num = int(input("imforme um numero: "))


def primo(num):
    for x in range(2, num):
        if num % 2 == 0:
            return print(num, 'não é primo')
        else:
            return print(num, 'é primo')

primo(num)
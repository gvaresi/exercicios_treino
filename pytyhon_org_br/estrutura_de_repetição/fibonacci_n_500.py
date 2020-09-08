"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

a = 0
b = 1
f = 0
while f < 2000:
    f = a + b
    a = b
    b = f

print('A sequncia de Fibonacci maior que 500 é: ', f)

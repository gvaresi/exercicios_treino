"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input("informe o n-ésimo de Fibonacci: "))
a = 0
b = 1
f = 0

for i in range(1, n+1):

    f = a + b
    a = b
    b = f

print('O n-énimo numero de Fibonacci é: ', f)

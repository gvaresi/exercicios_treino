"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""

for x in range(1, 21):
    print(x)
print()

y = []  # lista vazia antes do for pois depois dele ele vai zerar sempre e nao adicionara elementos
for x_1 in range(1, 21):
    y.append(x_1)
print(y)

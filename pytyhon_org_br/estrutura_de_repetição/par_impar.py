"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""


texto_impar = 'A quantidade de numeros impar são {0} e os numeros são: {1}'
texto_par = 'A quanidade de numeros par são {0} e os numeros são: {1}'

num_1 = int(input("digite um numero:"))
num_2 = int(input("digite um numero:"))
num_3 = int(input("digite um numero:"))
num_4 = int(input("digite um numero:"))
num_5 = int(input("digite um numero:"))
num_6 = int(input("digite um numero:"))
num_7 = int(input("digite um numero:"))
num_8 = int(input("digite um numero:"))
num_9 = int(input("digite um numero:"))
num_10 = int(input("digite um numero:"))

numeros = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]
impar = [num for num in numeros if num % 2 == 1]
par = [num for num in numeros if num % 2 == 0]

i = len(impar)
p = len(par)

print(texto_impar.format(i, sorted(impar)))
print(texto_par.format(p, sorted(par)))

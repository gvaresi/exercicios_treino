"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""


texto = 'O numéro {0} elevado a potência {1} da o resultado {2} '

num_1 = int(input('Digite um numero inteiro: '))
num_2 = int(input('Digite um numero expoente: '))
resultado = num_1


for e in range(1, num_2):
    resultado *= num_1


print(texto.format(num_1, num_2, resultado))

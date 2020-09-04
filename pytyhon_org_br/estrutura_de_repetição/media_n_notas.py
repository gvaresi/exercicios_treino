"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

texto = 'A media das {0} notas é {1}'
texto_1 = 'Informe a nota {0} :'


quant_notas = int(input("informe quantas notas serão informadas: "))
num_notas = 0
lista_notas = []

while quant_notas != num_notas:
    num_notas += 1
    notas = int(input(texto_1.format(num_notas)))
    while notas < 0 or not notas <= 10:
        notas = int(input(texto_1.format(num_notas)))
    lista_notas.append(notas)
media = (sum(lista_notas)) / quant_notas

print(texto.format(quant_notas, media))

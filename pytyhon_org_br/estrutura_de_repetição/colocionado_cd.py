"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""


texto_valor_cd = 'Quanto custou o cd numero {0}: '
texto_resposta = 'Para comprar {0} Cds o colecionador gastou R$ {1} e em media ele gastou R$ {2} em cada CD.'

quant_cd = int(input("Quantos CD's o Colecionador comprou? "))
lista_valor_cds = []

for x in range(1, quant_cd + 1):
    valor_cd = float(input(texto_valor_cd.format(x)))
    while valor_cd < 0:
        valor_cd = float(input(texto_valor_cd.format(x)))
    lista_valor_cds.append(valor_cd)

total_gasto = sum(lista_valor_cds)
media_unitario = total_gasto / quant_cd

print(texto_resposta.format(quant_cd, '%.2f' % total_gasto, '%.2f' % media_unitario))

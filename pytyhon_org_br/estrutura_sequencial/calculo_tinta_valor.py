"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
    """

print('Programa para calcular a quantidade de tinta necessaria para pintar por metro quadrado')
metro_quadrado = float(input('Informe o metro quadrado a ser pintado:'))
metro_quadrado_10 = metro_quadrado * 1.1

lata_18 = ((metro_quadrado_10 / 6) / 18) + .5
custo_lata_18 = 80
lata_3_6 = ((metro_quadrado_10 / 6) / 3.6) + .5
custo_lata_3_6 = 25

quant_litro = metro_quadrado_10 / 6
galao_18 = (quant_litro / 18) - .5  # quantidade de galoes nescessarios
resto = quant_litro - (18 * galao_18)  # quantidade total de litros dimiuido da quntidade de galoes de 18 litros
galao_3_6 = (resto / 3.6) + .51

valor_lata_18 = custo_lata_18 * round(lata_18)
valor_lata_3_6 = round(lata_3_6) * custo_lata_3_6
valor_lata_18_3_6 = (round(galao_18) * custo_lata_18) + (round(galao_3_6) * custo_lata_3_6)


if __name__ == '__main__':
    print('Você precisa de ', round(lata_18), ' galão de 18 litros no valor total de R$', round(valor_lata_18, 2))
    print('Você precisa de ', round(lata_3_6), ' galão de 3,6 litros no valor total de R$', round(valor_lata_3_6, 2))
    print('Você precisa de ', round(galao_18), ' galão de 18 litros e de', round(galao_3_6),
          'galão de 3,6 litros no valor total de R$', round(valor_lata_18_3_6, 2))
    print(galao_3_6)


prova_1 = (18 * lata_18) * 6
prova_2 = (3.6 * lata_3_6) * 6
prova_3 = ((18 * galao_18) + (3.6 * galao_3_6)) * 6

if __name__ == '__main__':
    print('Total de metros quadados adicionado 10 %:', round(metro_quadrado_10))
    print('Total de metros quadrados que essa quantidade de tinta cobre:', round(prova_1))
    print('Total de metros quadrados que essa quantidade de tinta cobre:', round(prova_2))
    print('Total de metros quadrados que essa quantidade de tinta cobre:', round(prova_3))

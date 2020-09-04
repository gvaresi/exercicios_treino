"""Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

print('Programa para calcular a quantidade de tinta necessaria para pintar um comodo')
metro_quadrado = float(input('Informe o metro quadrado do comodo:'))


galao_tinta = ((metro_quadrado / 3) / 18) + .5

if __name__ == '__main__':
    print('Você precisa de ', round(galao_tinta), 'latas de tinta de 18 litros')
    # print('Você precisa de ', (galao_tinta), 'de tintas com 18 litros')
    # print('galao tinta alterado', galao_tinta)
    # print('galao check', galao_check)

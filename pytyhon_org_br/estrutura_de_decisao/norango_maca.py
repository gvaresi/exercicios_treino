"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
    e escreva o valor a ser pago pelo cliente.
"""


morango = float(input('Informe quantos kilos o cliente comprou de morango :'))
maca = float(input('Informe quantos kilos o cliente comprou de maça :'))

if morango <= 5:
    custo_morango = morango * 2.5
else:
    custo_morango = morango * 2.2


if maca <= 5:
    custo_maca = maca * 2.5
else:
    custo_maca = maca * 2.2

valor_a_pagar = custo_morango + custo_maca

if valor_a_pagar > 25:
    valor_a_pagar *= .9

print('O valor a ser pago por,', morango, 'Kilos de morando e', maca, 'Kilos de maça, é de R$', '%.2f' % valor_a_pagar)

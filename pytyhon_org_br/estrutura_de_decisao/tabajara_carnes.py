"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                     Acima de 5 Kg             Até 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente.
    Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
     valor do desconto e valor a pagar.
"""


cupom_fiscal = """           *** Cupom Fiscal ***
      Tipo Carne        {0}
      Peso              {1} Kilo
      Preco Total       R$ {2}
      Pagamento         {3}
      Valor Desconto    R$ {4}
      Valor A Pagar     R$ {5}
      """
preco_total = float
escolhido = str

escolha = float(input("""Escolha o tipo da carne que o cliente escolheu:
                      1 - File duplo
                      2 - Alcatra
                      3 - Picanha:
                      """))

while escolha > 3 or escolha < 1:
    escolha = float(input("""Escolha o tipo da carne que o cliente escolheu:
                      1 - file duplo
                      2 - Alcatra
                      3 - Picanha:
                      """))

if escolha == 1:
    escolhido = 'File Duplo'
elif escolha == 2:
    escolhido = 'Alcatra'
elif escolha == 3:
    escolhido = 'Picanha'


kilo_carne = float(input('Informe o peso da carne: '))
while kilo_carne <= 0:
    kilo_carne = float(input('Informe o peso da carne: '))


cartao = input("""O pagamento vai ser com cartão Tabajara?
               S - Sim
               N - Não:

               """)
while 'S' != cartao != 'N':
    cartao = input("""O pagamento vai ser com cartão Tabajara?
               S - Sim
               N - Não:

               """)

if escolha == 1:
    if kilo_carne >= 5:
        preco_total = kilo_carne * 5.8
    else:
        preco_total = kilo_carne * 4.9

if escolha == 2:
    if kilo_carne >= 5:
        preco_total = kilo_carne * 6.8
    else:
        preco_total = kilo_carne * 5.9

if escolha == 3:
    if kilo_carne >= 5:
        preco_total = kilo_carne * 7.8
    else:
        preco_total = kilo_carne * 6.9


if cartao == 'S':
    desconto = preco_total * .05
    preco_a_pagar = preco_total - desconto
    tipo_pagamento = 'Cartao Tabajara'
else:
    tipo_pagamento = 'outros'
    desconto = 0
    preco_a_pagar = preco_total


print(cupom_fiscal.format(escolhido, kilo_carne, '%.2f' % preco_total, tipo_pagamento,
                          '%.2f' % desconto, '%.2f' % preco_a_pagar))

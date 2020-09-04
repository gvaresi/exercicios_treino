"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
    calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
    o preço do litro do álcool é R$ 1,90.
"""


gasolina = 2.50
alcool = 1.90
custo = 0
tipo = str

combustivel = input("""Informe o combustivel desejado:
                    A - Álcool ou 
                    G - Gasolina 
                    """)
while combustivel != 'A' and combustivel != 'G':
    combustivel = input("""Informe o combustivel desejado:
                    A - Álcool ou 
                    G - Gasolina 
                    """)
G = 'gasolina'
A = 'álcool'

                    
litros = float(input('Quantos litros foram abastecidos: '))

if combustivel == 'A':
    tipo = A
    if litros >= 20:
        custo = litros * (alcool * .97)
    else:
        custo = litros * (alcool * .95)
    
    
if combustivel == 'G':
    tipo = G
    if litros >= 20:
        custo = litros * (gasolina * .96)
    else:
        custo = litros * (gasolina * .94)

        
print('O cliente ir pagar R$', '%.2f' % custo, ', por ', int(litros), 'litros de', tipo)

"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
nota_1 = int
nota_5 = int
nota_10 = int
nota_50 = int
nota_100 = int

saque = int(input('Informe o valor para saque :'))
while saque > 600 or saque < 10:
    saque = int(input('Informe o valor para saque :'))

if saque >= 100:
    nota_100 = saque // 100
    nota_50 = ((saque - ((saque // 100) * 100)) // 50)
    nota_10 = (saque - ((nota_100 * 100) + (nota_50 * 50))) // 10
    nota_5 = (saque - ((nota_100 * 100) + (nota_50 * 50) + (nota_10 * 10))) // 5
    nota_1 = (saque - ((nota_100 * 100) + (nota_50 * 50) + (nota_10 * 10) + (nota_5 * 5))) // 1
elif saque < 100:
    nota_50 = saque // 50
    nota_10 = (saque - (nota_50 * 50)) // 10
    nota_5 = (saque - ((nota_50 * 50) + (nota_10 * 10))) // 5
    nota_1 = (saque - ((nota_50 * 50) + (nota_10 * 10) + (nota_5 * 5))) // 1
elif saque < 50:
    nota_10 = saque // 10
    nota_5 = (saque - (nota_10 * 10)) // 5
    nota_1 = (saque - (nota_10 * 10) + (nota_5 * 5)) // 1
elif saque == 10:
    nota_10 = saque // 10


if __name__ == '__main__':
    if nota_100 != 0:
        print('Nota R$ 100,00 = ', nota_100)
    if nota_50 != 0:
        print('Nota R$ 50,00 = ', nota_50)
    if nota_10 != 0:
        print('Nota R$ 10,00 = ', nota_10)
    if nota_5 != 0:
        print('Nota R$ 5,00 = ', nota_5)
    if nota_1 != 0:
        print('Nota R$ 1,00 = ', nota_1)

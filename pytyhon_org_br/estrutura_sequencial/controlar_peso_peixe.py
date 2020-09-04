"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
 o valor da multa que João deverá pagar.

Imprima os dados do programa com as mensagens adequadas.
"""

peso_permitido = float(50)
valor_multa = float(4.00)

peso_pescado = float(input("Informe o peso Pescado no dia:"))

dif_peso = (peso_pescado - peso_permitido)
if 0 < dif_peso:
    multa = (dif_peso * valor_multa)
    print('O peso exedente é de ', dif_peso, 'KG')
    print('O valor da multa para pagamento hoje é R$', ('%.2f' % multa))
else:
    print('O peso do dia é inferior a', peso_permitido, 'não tem multa a pagar.')

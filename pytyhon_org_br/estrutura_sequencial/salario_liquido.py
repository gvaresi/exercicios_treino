"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
print('Programa para calculo de salario bruto e liquido')

valor_hora = float(input('informe o valor da hora trabalhada:'))
horas_trabalhada = float(input('informe quantas horas trabalhadas no mês:'))
salario_bruto = (valor_hora * horas_trabalhada)
ir = (salario_bruto * .11)
inss = (salario_bruto * .08)
sindicato = (salario_bruto * .05)
salario_liquido = (salario_bruto - (ir + inss + sindicato))


"""
expressão para mostrar duas casas decimais. print("%.2f" % round(a,2)),
omde 'a' é a variavel e a expressao round serve para aredondar
"""

print('+ Salário Bruto : R$ ', "%.2f" % round(salario_bruto, 2))
print('- IR : R$ ', "%.2f" % round(ir, 2))
print('- INSS : R$ ', "%.2f" % round(inss, 2))
print('- Sindicato : R$ ', "%.2f" % round(sindicato, 2))
print('- Salário liquido : R$ ', "%.2f" % round(salario_liquido, 2))

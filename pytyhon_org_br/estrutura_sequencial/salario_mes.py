"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

"""
custo_hora = float(input('Informe o valor da hora trabalhada: '))
dias_trabalhados = float(input('Informe quantos dias trabalhou no mes: '))
horas_trabalhados = float(input('Informe quantas horas trabalhou por dia: '))

"""
Horas_trabalhadas = float(input('Informe a quantidades de horas trabalhadas no mes : '))
"""


if __name__ == '__main__':
    rec_mes = (dias_trabalhados * horas_trabalhados) * custo_hora
    print('O valor a receber esse mes é : ', rec_mes)

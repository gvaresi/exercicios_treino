"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)  e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
            """

relatorio = """
            Salário Bruto:({0} * {1})       : R$ {2}
            - IR ({3}'%)                     : R$ {4}
            - Sindicarto ( 3 %)             : R$ {5}
            - INSS ( 10 %)                  : R$ {6}
            FGTS ( 11 %)                    : R$ {7}
            Total dos descontos             : R$ {8}
            Salário liquido                 : R$ {9}
"""

valor_hora = float(input('Informe o valor da hora trabalhada :'))
hora_trabalhada = float(input('Informe a quantidade de horas trabalhadas no mes :'))
salario_bruto = valor_hora * hora_trabalhada
ir = float
inss = salario_bruto * .1
fgts = salario_bruto * .11
sindicato = salario_bruto * .03

if __name__ == '__main__':
    if salario_bruto <= 900:
        ir = 0
    elif 900 < salario_bruto < 1500:
        ir = 5
    elif 1500 < salario_bruto < 2500:
        ir = 10
    elif salario_bruto > 2500:
        ir = 20
    desc_ir = (ir / 100) * salario_bruto
    descontos = desc_ir + sindicato + inss
    salario_liquido = salario_bruto - descontos
    print(relatorio.format('%0.f' % valor_hora, '%0.f' % hora_trabalhada, '%.2f' % salario_bruto, ir,
                           '%.2f' % desc_ir, '%.2f' % sindicato, '%.2f' % inss, '%.2f' % fgts, '%.2f' % descontos,
                           '%.2f' % salario_liquido))

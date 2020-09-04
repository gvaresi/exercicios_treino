"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
 e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
     baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""


texto_salario = """
Salário Base                    R$: {0}
Percentual aplicado no aumento:     {1} %
Valor do aumento no salário:    R$ {2}
Valor do salário com aumento:   R$ {3}
"""

salario_base = float(input("Informe o salario recebido:"))
salario_reajustado = 0
percentual = 0




if __name__ == '__main__':
    if salario_base <= 280:
        salario_reajustado = salario_base * 1.2
        percentual = 20
    elif salario_base <= 700:
        salario_reajustado = salario_base * 1.15
        percentual = 15
    elif salario_base <= 1500:
        salario_reajustado = salario_base * 1.1
        percentual = 10
    elif salario_base > 1500:
        salario_reajustado = salario_base * 1.05
        percentual = 5
    reajuste = salario_reajustado - salario_base

    print(texto_salario.format('%.2f' % salario_base,  percentual, '%.2f' % reajuste, '%.2f' % salario_reajustado))

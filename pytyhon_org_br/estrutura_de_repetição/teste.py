salario = float(input('Digite seu salario: '))

faixas = {'f1': 0.2, 'f2': 0.15, 'f3': 0.1, 'f4': 0.05}


def calcula_aumento(salario):
    """Retorna taxa e aumento."""
    if salario <= 280:
        taxa = faixas['f1']
    elif salario < 700:
        taxa = faixas['f2']
    elif salario < 1500:
        taxa = faixas['f3']
    elif salario >= 1500:
        taxa = faixas['f4']

    aumento = salario * taxa

    return taxa, aumento


taxa, aumento = calcula_aumento(salario)

print(f'Salário antes ddo reajuste é R$ {salario}')
print(f'Percentual de aumento {taxa * 100}%')
print(f'Valor do aumento: R$ {aumento}')
print(f'Novo salário: R$ {salario + aumento}')

"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input('digite o dia :'))
mes = int(input('digite o mes :'))
ano = int(input('digite o ano :'))

bissexto = (ano // 4) * 4

if __name__ == '__main__':
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 31 >= dia >= 1:
            if ano > 0:
                print('A Data ', dia, '/', mes, '/', ano, 'é Valida')

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 30 > dia > 1:
            if ano > 0:
                print('A Data ', dia, '/', mes, '/', ano, 'é Valida')

    if mes == 2 and ano != bissexto:
        if 28 >= dia >= 1:
            if ano > 0:
                print('A Data ', dia, '/', mes, '/', ano, 'é Valida')

    if mes == 2 and ano == bissexto:
        if 29 >= dia >= 1:
            if ano > 0:
                print('A Data ', dia, '/', mes, '/', ano, 'é Valida')

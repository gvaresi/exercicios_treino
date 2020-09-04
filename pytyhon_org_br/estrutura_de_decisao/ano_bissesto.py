"""
Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto.
"""

ano = int(input('Digite um ano :'))


while ano < 0:
    ano = int(input('Digite um ano :'))

bissexto = (ano // 4) * 4

if __name__ == '__main__':
    if ano == bissexto:
        print('Ano ', ano, 'é bissexto')
    else:
        print('Ano ', ano, 'não é bissexto')

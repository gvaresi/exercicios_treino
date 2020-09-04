"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

matutino = ('m')
vespertino = ('v')
noturno = ('n')
"""

periodo = str(input('Qual turno voce estuda "M" -matutino ou "V" -Vespertino ou "N" - Noturno: '))

while 1 != len(periodo):
    periodo = str(input('Qual turno voce estuda "M" -matutino ou "V" -Vespertino ou "N" - Noturno: '))


if __name__ == '__main__':
    if periodo == 'm' or periodo == 'M':
        print("Bom Dia!")
    elif periodo == 'v' or periodo == 'V':
        print('Boa Tarde!')
    elif periodo == 'n' or periodo == 'N':
        print('Boa Noite!')
    else:
        print('Horario Inválido!')

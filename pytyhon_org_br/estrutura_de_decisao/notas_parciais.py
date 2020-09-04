"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_1 = float(input('Informa a nota do primeiro bimestre :'))
while nota_1 > 10:
    nota_1 = float(input('Informa a nota do primeiro bimestre :'))


nota_2 = float(input('Informa a nota do segundo bimestre :'))
while nota_2 > 10:
    nota_2 = float(input('Informa a nota do segundo bimestre :'))

media = (nota_1 + nota_2) / 2
if __name__ == '__main__':
    if media == 10:
        print('O aluno teve a media de', media, 'sendo aprovado com louvor')
    elif media >= 7:
        print('O aluno teve a media de', media, 'sendo aprovado')
    else:
        print('O aluno teve a media de', media, 'sendo reprovado')

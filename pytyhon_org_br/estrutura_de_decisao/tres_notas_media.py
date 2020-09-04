"""
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota_1 = float(input('Digite a nota da primeira parcial :'))
while nota_1 > 10 or nota_1 < 0:
    nota_1 = float(input('Digite a nota da primeira parcial :'))

nota_2 = float(input('Digite a nota da segunda parcial :'))
while nota_2 > 10 or nota_2 < 0:
    nota_2 = float(input('Digite a nota da segunda parcial :'))

nota_3 = float(input('Digite a nota da terceira parcial :'))
while nota_3 > 10 or nota_3 < 0:
    nota_3 = float(input('Digite a nota da terceira parcial :'))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print('Media = ', media, ' - Aprovado com Distinção')
elif 10 > media >= 7:
    print('Media = ', "%.2f" % media, ' - Aprovado')
else:
    print('Media = ', "%.2f" % media, ' - Reprovado')

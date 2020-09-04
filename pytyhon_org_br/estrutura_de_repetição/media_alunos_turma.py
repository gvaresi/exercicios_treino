"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

texto_alunos_turma = 'Quantos alunos possue a turma {0}: '
texto_final = 'Em {0} turmas a quantidde media de alunos é {1}.'

quantidade_turmas = int(input('Quantas turmas existem: '))
lista_alunos = []


for x in range(1, quantidade_turmas + 1):
    quantidade_alunos = int(input(texto_alunos_turma.format(x)))

    while quantidade_alunos > 40:
        print('Numero maximo de alunos por turma nao pode passar de 40.')
        quantidade_alunos = int(input(texto_alunos_turma.format(x)))
    lista_alunos.append(quantidade_alunos)

media_alunos = (sum(lista_alunos)) / quantidade_turmas
print(texto_final.format(quantidade_turmas, '%.f' % media_alunos))


"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"s
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder posnaoitivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

n=str('n')
s=str('s')
"""

quest_1 = str(input('Você telefonou para a vitima? "s" - sim ou "n" para não: '))
while 's' != quest_1 != 'n':
    quest_1 = str(input('Você telefonou para a vitima? digita apenas "s" - sim ou "n" para não: '))

quest_2 = str(input('Você telefonou para a vitima? "s" - sim ou "n" para não: '))
while 's' != quest_2 != 'n':
    quest_2 = str(input('Você telefonou para a vitima? digita apenas "s" - sim ou "n" para não: '))

quest_3 = str(input('Você telefonou para a vitima? "s" - sim ou "n" para não: '))
while 's' != quest_3 != 'n':
    quest_3 = str(input('Você telefonou para a vitima? digita apenas "s" - sim ou "n" para não: '))

quest_4 = str(input('Você telefonou para a vitima? "s" - sim ou "n" para não: '))
while 's' != quest_4 != 'n':
    quest_4 = str(input('Você telefonou para a vitima? digita apenas "s" - sim ou "n" para não: '))

quest_5 = str(input('Você telefonou para a vitima? "s" - sim ou "n" para não: '))
while 's' != quest_5 != 'n':
    quest_5 = str(input('Você telefonou para a vitima? digita apenas "s" - sim ou "n" para não: '))


resp = [quest_1, quest_2, quest_3, quest_4, quest_5]
resp.sort()
s_total = resp.count('s')
print()

if __name__ == '__main__':
    if s_total == 5:
        print('Culpado')
    elif 4 >= s_total >= 3:
        print('Cúmplice')
    elif s_total == 2:
        print('Suspeita')
    else:
        print('Inocente')

"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

masculino = 'm'
feminino = 'f'

print('Modulo calcula peso ideal entra homes e mulhres')

escolha = str(input('Digite o seu sexo "M" - masculino, "F" feminino : '))


while 1 != len(escolha):
    escolha = str(input('Digite o seu sexo "M" - masculino, "F" feminino : '))


if escolha == masculino:
    alt_masc = float(input('Informe a sua altura : '))
    peso_h = (72.7 * alt_masc) - 58
    print('O peso idel para Homens acom a altura de', alt_masc, 'M é de', round(peso_h, 2), 'KG')
else:
    if escolha == feminino:
        alt_fem = float(input('Informe a sua altura : '))
        peso_f = (72.7 * alt_fem) - 44.7
        print('O peso idel para Mulheres com a altura de', alt_fem, 'M é de', round(peso_f, 2), 'KG')

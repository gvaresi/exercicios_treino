"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
print('Calcular media bimestral de 4 bimestres:')

bim_1 = float(input('Digite a Nota do Primeiro Bimestre:'))
bim_2 = float(input('Digite a Nota do Segundo Bimestre:'))
bim_3 = float(input('Digite a Nota do Terceiro Bimestre:'))
bim_4 = float(input('Digite a Nota do Quarto Bimestre:'))

media = (bim_1+bim_2+bim_3+bim_4) / 4

if __name__ == '__main__':
    print('Media da Nota Bimestral:', media)

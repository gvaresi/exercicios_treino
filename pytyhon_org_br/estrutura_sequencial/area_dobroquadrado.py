"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado = float(input('Digite o Tamanho do Lado do Quadrado em Cm² : '))

area_quadrado = lado*lado
area_quadrado_2 = area_quadrado * 2

metros_1 = (lado / 100) * 2
metros_2 = metros_1 * 2

if __name__ == '__main__':
    print('Area do Quadrado: ', area_quadrado, 'cm²', ' - Dobro da Area do Quadrado : ', area_quadrado_2, 'cm²')
    print('Area do Quadrado Convertido em Metros: ', metros_1, 'm²',
          ' - Dobro da Area do Quadrado em Metros: ', metros_2, 'm²')

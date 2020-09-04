"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
print("Calculo do peso ideal refenfente a altura")
altura = float(input('Digite sua altura: '))

peso_ideal = (72.7 * altura) - 58

if __name__ == '__main__':
    print('Seu peso ideal seria : ', peso_ideal, 'KG')

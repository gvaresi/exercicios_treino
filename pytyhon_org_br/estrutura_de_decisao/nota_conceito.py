"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
    se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota_1 = float(input('Digite a nota do primeira parcial :'))
nota_2 = float(input('Digite a nota do segunda parcial :'))
media = (nota_2 + nota_1) / 2


while 0 > media > 10:
    nota_1 = float(input('Digite a nota do primeira parcial:'))
    nota_2 = float(input('Digite a nota do segunda parcial:'))
    media = (nota_1 + nota_2) / 2


print('Nota primeira parcial :', nota_1)
print('Nota segunda parcial :', nota_2)
print('Media da nota :', media)


if __name__ == '__main__':
    if 10 >= media >= 9:
        print('conceito A')
        print('Aprovado')
    elif 9 > media >= 7.5:
        print('conceito B')
        print('Aprovado')
    elif 7.5 > media >= 6:
        print('conceito C')
        print('Aprovado')
    elif 6 > media >= 4:
        print('conceito D')
        print('Reprovado')
    elif 4 > media >= 0:
        print('conceito E')
        print('Reprovado')

"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

   par ou ímpar;
   positivo ou negativo;
   inteiro ou decimal.
"""

num_1 = int(input('Digite o primeiro numero: '))
num_2 = int(input('Digite o segundo numero: '))
resultado = float
operacao = input("""Escolha a operção:
                 '+' - para adição :
                 '-' - para subtração :
                 '*' - para multiplicação :
                 '/' - para divisão :
                 """)

while not operacao == '/' and not operacao == '*' and not operacao == '-' and not operacao == '+':
    operacao = input("""Escolha a operção:
                 '+' - para adição :
                 '-' - para subtração :
                 '*' - para multiplicação :
                 '/' - para divisão :
                 """)


if operacao == '/':
    resultado = num_1 / num_2
elif operacao == '*':
    resultado = num_1 * num_2
elif operacao == '+':
    resultado = num_1 + num_2
elif operacao == '-':
    resultado = num_1 - num_2 

if resultado % 2 == 0:
    par_impar = 'par'
else:
    par_impar = 'impar'

if resultado >= 0:
    fator = "positivo"
else:
    fator = 'negativo'

if type(resultado) == int:
    tipo = 'inteiro'
else:
    tipo = 'decimal'


print('O resultado da operação pedida é', resultado, ', ele é ', par_impar, ', ', fator, 'e ', tipo)

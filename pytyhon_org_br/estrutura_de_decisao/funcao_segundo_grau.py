"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
    e o programa não deve fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""

a = float(input('Digite o valor de "a" :'))
while a == 0:
    a = float(input('O valor de "a" não pode ser 0 :'))

b = float(input('Digite o valor de "b" :'))
c = float(input('Digite o valor de "c" :'))

delta = b ** 2 - (4 * a * c)
if delta < 0:
    print('O Delta é negativo portanto o programa será encerrado')
    exit()

if delta == 0:
    print('O Delta é igual a zero entao nao possu raiz real nesse caso o programa será encerrado')
    exit()

x_1 = ((b ** 2) + delta) / (2 * a)
x_2 = ((b ** 2) - delta) / (2 * a)

print('A primeira raiz real é :', x_1)
print('A segunda raiz real é :', x_2)

"""
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com:
                        326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


uni = 'unidade'
unis = 'unidades'
cen = 'centena'
cens = 'centenas'
dez = 'dezena'
dezs = 'dezenas'

numero = int(input("digite um numero menor que 1000 :"))

while numero >= 1000:
    numero = int(input("digite um numero menor que 1000 :"))

centena = (numero // 100) * 100
dezena = ((numero - centena) // 10) * 10
unidade = (numero - centena - dezena)
cent_p = 'um'
dez_p = 'dois'
uni_p = 'tres'


if __name__ == '__main__':
    if centena == 100:
        cent_p = cen
    else:
        cent_p = cens
    if dezena <= 10:
        dez_p = dez
    else:
        dez_p = dezs
    if unidade <= 1:
        uni_p = uni
    else:
        uni_p = unis
    if centena == 0 and unidade == 0:
        print(numero, '=', (dezena // 10), dez_p)
    elif centena == 0 and dezena == 0:
        print(numero, '=', unidade, uni_p)
    elif centena == 0:
        print(numero, '=', (dezena // 10), dez_p, 'e', unidade, uni_p)
    elif dezena == 0 and unidade == 0:
        print(numero, '=', (centena // 100), cent_p)
    elif dezena == 0:
        print(numero, '=', (centena // 100), cent_p, 'e', unidade, uni_p)
    elif unidade == 0:
        print(numero, '=', (centena // 100), cent_p, 'e', (dezena // 10), dez_p)
    else:
        print(numero, '=', (centena // 100), cent_p, ',', (dezena // 10), dez_p, 'e', unidade, uni_p)

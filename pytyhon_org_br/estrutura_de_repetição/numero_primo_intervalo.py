"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
num_1 = int(input('Informe um numero: '))
primo = 'O numero   {0}     é primo.'
nao_primo = 'O numero   {0}     não é primo.'




def numero(n: int):
    for n_1 in range(1, n + 1):

        def numero_1(d: int):
            list_num = []
            for d_1 in range(1, d + 1):
                if n_1 % d_1 == 0:
                    list_num.append(d_1)
            if len(list_num) == 2:
                return print(primo.format(n_1))
            else:
                return print(nao_primo.format(n_1))

        numero_1(num_1)


numero(num_1)

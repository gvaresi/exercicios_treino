"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

num_1 = int(input('Informe um numero: '))
primo = 'O numero   {0}     é primo porque ele é so  divisivel pelos seguintes numeros {1}.'
nao_primo = 'O numero   {0}     não é primo porque ele é divisivel pelos seguintes numeros {1}.'


def numero(n: int):
    for n_1 in range(1, n + 1):

        def numero_1(d: int):
            list_num = []
            for d_1 in range(1, d + 1):
                if n_1 % d_1 == 0:
                    list_num.append(d_1)
            if len(list_num) == 2:
                return print(primo.format(n_1, list_num))
            else:
                return print(nao_primo.format(n_1, list_num))

        numero_1(num_1)


numero(num_1)

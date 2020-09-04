"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
"""


def tabuada(t: int):
    for x in range(1, t + 1):
        print()
        print('Tabuada do', x, ':')
        for n in range(1, t + 1):
            result = x * n
            print(x, 'X', n, '=', result)
                
       
tabuada(10)

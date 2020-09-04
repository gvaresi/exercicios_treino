"""
Fazer um jogo da velha
"""

tabuleiro = """
                            |      |
                        {0}   |  {1}   |  {2}
                      ______|______|______
                            |      |
                        {3}   |  {4}   |  {5}  
                      ______|______|______
                            |      |
                        {6}   |  {7}   |  {8}  
                            |      |
                                            :
"""


np = 's'
while np == 's':

    t = 7
    y = 8
    z = 9
    a = 4
    b = 5
    c = 6
    h = 1
    i = 2
    j = 3
    rep = []

    for v in range(1, 6):
        print('Jogador 01')
        n = int(input(tabuleiro.format(t, y, z, a, b, c, h, i, j)))

        while n < 1 or n > 9 or n in rep:
            print('Jogador 01 - Posição invalida ou não disponivel')
            n = int(input(tabuleiro.format(t, y, z, a, b, c, h, i, j)))

        if n == 7:
            t = 'O'
        elif n == 8:
            y = 'O'
        elif n == 9:
            z = 'O'
        elif n == 4:
            a = 'O'
        elif n == 5:
            b = 'O'
        elif n == 6:
            c = 'O'
        elif n == 1:
            h = 'O'
        elif n == 2:
            i = 'O'
        elif n == 3:
            j = 'O'

        rep.append(n)

        if t == y == z:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif a == b == c:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif h == i == j:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif t == a == h:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif y == b == i:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif z == c == j:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
        elif t == b == j:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif z == b == h:
            print('Fim de Jogo Vencedor Jogador 01', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break

        if v == 5:
            print('Empate', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        print('Jogador 02')
        m = int(input(tabuleiro.format(t, y, z, a, b, c, h, i, j)))

        while m < 1 or m > 9 or m in rep:
            print('Jogador 02 - Posição invalida ou não disponivel')
            m = int(input(tabuleiro.format(t, y, z, a, b, c, h, i, j)))

        if m == 7:
            t = 'X'
        elif m == 8:
            y = 'X'
        elif m == 9:
            z = 'X'
        elif m == 4:
            a = 'X'
        elif m == 5:
            b = 'X'
        elif m == 6:
            c = 'X'
        elif m == 1:
            h = 'X'
        elif m == 2:
            i = 'X'
        elif m == 3:
            j = 'X'

        rep.append(m)

        if t == y == z:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif a == b == c:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif h == i == j:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif t == a == h:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif y == b == i:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif z == c == j:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif t == b == j:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break
        elif z == b == h:
            print('Fim de Jogo Vencedor Jogador 02', tabuleiro.format(t, y, z, a, b, c, h, i, j))
            break

    np = str(input('Deseja jogar novamente? s - sim '))

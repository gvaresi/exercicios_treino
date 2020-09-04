"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

texto_voto = """
                informe o voto no seu candidato
                pava votar no:
                candidato Abobrinha  digite - 11
                candidato Berinjela  digite - 21
                candidato Alcachofra digite - 31
"""
texto_candidato_nao_existe = """
                Candidado não existe
"""

eleitores = int(input('Informe o total de eleitores: '))
votos = []
candidato_1 = []
candidato_2 = []
candidato_3 = []
voto = int


for x in range(1, eleitores + 1):
    voto = int(input(texto_voto))
    while voto != 11 and voto != 21 and voto != 31:
        print(texto_candidato_nao_existe)
        voto = int(input(texto_voto))
    if voto == 11:
        candidato_1.append(voto)
    elif voto == 21:
        candidato_2.append(voto)
    elif voto == 31:
        candidato_3.append(voto)


print('O candidato Abobrinha recebeu: ', len(candidato_1), 'votos')
print('O candidato Berinjela  recebeu: ', len(candidato_2), 'votos')
print('O candidato Alcachofra recebeu: ', len(candidato_3), 'votos')

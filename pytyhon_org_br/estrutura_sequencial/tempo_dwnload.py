"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

print('Calcular o tempo do download de arquivo pela velocidade de download')

tamanho = float(input('Informe o tamanho do arquivo para download em MB:'))
velocidade = float(input('Informe a velocidade de download da sua internet em mbps:'))
velo_minutos = (tamanho / velocidade) / 60 + .5

if __name__ == '__main__':
    print('O temopo estimado para o termino do download do arquivo com',
          round(tamanho), 'MB é de aprocimadamente', round(velo_minutos), 'minutos')

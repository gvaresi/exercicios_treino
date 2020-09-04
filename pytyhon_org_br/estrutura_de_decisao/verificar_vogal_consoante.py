"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = str(input('Digite uma letra qualquer : '))
vogal = ("a" or "e" or "i" or "o" or "u")

while 1 != len(letra):
    letra = str(input('Digite uma letra qualquer : '))


if __name__ == '__main__':
    if letra == vogal:
        print('A letra', letra, 'é vogal')
    else:
        print('A letra', letra, 'é uma consoante')

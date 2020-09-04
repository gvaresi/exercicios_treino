"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = str(input('Digite "F" para Feminino e "M" para Masculino : '))
f = 'f'
m = 'm'

while 1 != len(sexo):
    sexo = str(input('Digite "F" para Feminino e "M" para Masculino : '))

if __name__ == '__main__':
    if f == sexo:
        print('Feminino')
    elif sexo == m:
        print('Masculino')
    else:
        print('Sexo indefinido')

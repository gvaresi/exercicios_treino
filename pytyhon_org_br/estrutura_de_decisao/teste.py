# teste


texto = '{0} tem {idade} anos de idade'
print('Progama para calcular a idade de uma pessoa')
print()

nome = input('Entre com o nome da pessoa: ')
print()

a1 = int(input("Entre com o ano de nascimento: "))
print()

a2 = int(input("Entre com ano atual: "))
print()
print(texto.format(nome, idade=a2 - a1))

"""
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
texto_pergunta_idade = 'Informe a idade da {0} pessoa: '
x = str
y = 1
lista_idade_0_25 = []
lista_idade_26_60 = []
lista_idade_Maior_60 = []


while x != 'n':
    idade = int(input(texto_pergunta_idade.format(y)))
    y += 1
    x = str(input('Deseja informar mais idades? s - Sim / n - Náo '))
    if 0 < idade <= 25:
        lista_idade_0_25.append(idade)
    elif 25 < idade <= 60:
        lista_idade_26_60.append(idade)
    else:
        lista_idade_Maior_60.append(idade)







print(lista_idade_0_25)
print(lista_idade_26_60)
print(lista_idade_Maior_60)
print(y)
print(x)
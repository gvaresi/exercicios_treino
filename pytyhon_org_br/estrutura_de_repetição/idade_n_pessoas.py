"""
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

texto_final = 'A media das idades é {0} e pela meddia essa turma é {1}'
texto_pergunta_idade = 'Informe a idade da {0} pessoa: '
x = str
y = 1
lista_idade = []
media_idade = int

while x != 'n':
    idade = int(input(texto_pergunta_idade.format(y)))
    x = str(input('Deseja informar mais idades? s - Sim / n - Náo '))
    lista_idade.append(idade)
    media_idade = sum(lista_idade) / y
    y += 1

if 0 < media_idade <= 25:
    print(texto_final.format(y - 1, '%.f' % media_idade), 'essa turma é jovem')
elif 25 < media_idade <= 60:
    print(texto_final.format(y - 1, '%.f' % media_idade), 'essa turma é adulta')
else:
    print(texto_final.format(y - 1, '%.f' % media_idade), 'essa turma é idosa')

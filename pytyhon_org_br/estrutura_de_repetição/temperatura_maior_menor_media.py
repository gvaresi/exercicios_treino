"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

texto = """
A menor temperatura registrada foi de   {0} Graus
A maior temperatura registrada foi de   {1} Graus
A media da temperatura registrada foi de {2} Graus
"""

temperatura = float
mais_temperatura = 's'
lista_temp = []

while mais_temperatura == 's':
    temperatura = float(input('Informe uma temperatura: '))
    lista_temp.append(temperatura)
    mais_temperatura = input('Deseja informar mais uma temperatura: s - Sim ')

lista_temp.sort()
print(texto.format(lista_temp[0], lista_temp[-1], '%.1f' % (sum(lista_temp) / len(lista_temp))))

"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
"""

num_1 = int(input('Informe um numero: '))
num_2 = int(input('Informe um numero: '))
num_3 = int(input('Informe um numero: '))
num_4 = int(input('Informe um numero: '))
num_5 = int(input('Informe um numero: '))
num_6 = int(input('Informe um numero: '))
num_7 = int(input('Informe um numero: '))
num_8 = int(input('Informe um numero: '))
num_9 = int(input('Informe um numero: '))
num_10 = int(input('Informe um numero: '))

numeros = [num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10]

numeros.sort()

soma = numeros[0] + numeros[-1]

texto = """
            Dado a lista de numeros a seguir    {0} 
            o menor numero é                    {menor}
            o maior numero é                    {maior}
            o resultado sa soma deles é         {1}
            """


print(texto.format(numeros, soma, menor=numeros[0], maior=numeros[-1]))

"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

num_1 = int(input('Informe um numero estre 0 e 1000: '))
while num_1 < 0 or num_1 > 1000:
    num_1 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_2 = int(input('Informe um numero estre 0 e 1000: '))
while num_2 < 0 or num_2 > 1000:
    num_2 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_3 = int(input('Informe um numero estre 0 e 1000: '))
while num_3 < 0 or num_3 > 1000:
    num_3 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_4 = int(input('Informe um numero estre 0 e 1000: '))
while num_4 < 0 or num_4 > 1000:
    num_4 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_5 = int(input('Informe um numero estre 0 e 1000: '))
while num_5 < 0 or num_5 > 1000:
    num_5 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_6 = int(input('Informe um numero estre 0 e 1000: '))
while num_6 < 0 or num_6 > 1000:
    num_6 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_7 = int(input('Informe um numero estre 0 e 1000: '))
while num_7 < 0 or num_7 > 1000:
    num_7 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_8 = int(input('Informe um numero estre 0 e 1000: '))
while num_8 < 0 or num_8 > 1000:
    num_8 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_9 = int(input('Informe um numero estre 0 e 1000: '))
while num_9 < 0 or num_9 > 1000:
    num_9 = int(input('Digite novamente so numero estre 0 e 1000: '))

num_10 = int(input('Informe um numero estre 0 e 1000: '))
while num_10 < 0 or num_10 > 1000:
    num_10 = int(input('Digite novamente so numero estre 0 e 1000: '))


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

"""
Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!"
"""


st = 'Print every word in this sentence that has an even number of letters'

for pa_par in st.split():  # onde .split significa desmembrar
    if len(pa_par) % 2 == 0:
        print(pa_par)

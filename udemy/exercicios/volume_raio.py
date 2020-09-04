"""
Escreva uma função que calcula o volume de uma esfera dado seu raio.
"""
raio = float(input("informe um valor para o raio: "))


def vol(rad):
    volume = (4 / 3) * 3.14 * rad ** 3
    return print(volume)


vol(raio)

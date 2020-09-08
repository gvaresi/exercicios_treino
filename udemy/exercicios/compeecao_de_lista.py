"""
Created on Wed Aug 12 16:25:50 2020

@author: Gian
"""

x = []

for i in range(0, 31):
    x += [i]
print(x)

print()
print()


x2 = [j for j in range(0, 11)]
print(x2)


print()
print()

x3 = [h * 2 + 10 for h in range(0, 15)]
print(x3)

print()
print()
x4 = [k * 4 + 25 for k in range(4, 24)]
print(x4)
print()
print()

x5 = [g for g in range(0, 100) if g % 3 == 2]
print(x5)


print()
print()

lista = [letra for letra in 'mundo universo']
print(lista)

print()
print()


celsius = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100]

fahrenreit = [temp * (9 / 5) + 32 for temp in celsius]
print(fahrenreit)

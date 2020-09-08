"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""


relatorio = """ *** Relatorio ***
                Nome            {0}
                Idade           {1}
                Salário         R$ {2}
                Sexo            {3}
                Estado Civil    {4}
                """
f = 'Feminino'
m = 'Masculino'
s = 'Solteiro(a)'
c = 'Casado(a)'
v = 'Viuvo(a)'
d = 'Divorciado(a)'


nome = input("Digite o seu nome:")
while len(nome) < 3:
    nome = input("Digite o seu nome:")

idade = int(input('Digite a sua idade: '))
while 0 > idade or idade > 150:
    idade = int(input('Digite a sua idade: '))


salario = float(input('Informe o salário: '))
while salario < 0:
    salario = float(input('Informe o salário: '))

sexo = input("""Sexo
             f - Feminino
             m - Masculino
             """)
while sexo != 'f' and sexo != 'm':
    sexo = input("""Sexo
                 f - Feminino
                 m - Masculino
                 """)

est_civil = input(""" Estado Civil
                  s - Solteiro(a)
                  c - Casado(a)
                  v - Viuvo(a)
                  d - Divorciado(a)
                  """)
while est_civil != 's' and est_civil != 'c' and est_civil != 'v' and est_civil != 'd':
    est_civil = input(""" Estado Civil
                      s - Solteiro(a)
                      c - Casado(a)
                      v - Viuvo(a)
                      d - Divorciado(a)
                      """)
if sexo == 'f':
    seho = f
else:
    sexo = m


if est_civil == 's':
    est_civil = s
elif est_civil == 'c':
    est_civil = c
elif est_civil == 'v':
    est_civil = v
else:
    est_civil = d


print(relatorio.format(nome, idade, '%.2f' % salario, sexo, est_civil))

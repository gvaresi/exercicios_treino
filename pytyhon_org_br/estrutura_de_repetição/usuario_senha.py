"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
import getpass

usuario = input('digite um nome de usuário: ')
senha = getpass.getpass('Digite uma senha: ')

while usuario == senha:
    print('A senha não pode ser igual ao nome!')
    senha = input('Digite uma senha: ')

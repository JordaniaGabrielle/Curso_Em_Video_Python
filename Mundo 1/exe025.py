# crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Qual o seu nome completo: ')

sobrenome = nome.lower()

if 'silva' in sobrenome:
    print('Existe a palavra "Silva" no seu nome')

else:
    print('Não existe a palavra "Silva" no seu nome')
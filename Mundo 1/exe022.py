# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minú´sculas.
# Quantas letras ao todo (Sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

print(f'Seu nome em maiúsculas é: {nome.upper()}')

print(f'Seu nome em maiúsculas é: {nome.lower()}')

print(f'Seu nome tem ao todo {len(nome)} letras')

nome_separado = nome.split()

print(f'Seu primeiro nome é {nome_separado[0]} ')

# faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite seu nome completo: ').strip()

nome2 = nome.split()

print(f'Seu primeiro nome é : {nome2[0]}')

print(f'Seu primeiro nome é : {nome2[len(nome2)-1]}')
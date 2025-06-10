# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ela podem
# ou não formar um triângulo.

r1 = int(input('Digite o comprimento da primeira reta:  '))
r2 = int(input('Digite o comprimento da segunda reta:  '))
r3 = int(input('Digite o comprimento da terceira reta:  '))

if r1 < r2 + r3 and r2 < r1 + r2:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')





# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Impar

numero = int(input('Digite um número para saber se ele é impar ou par  '))

if numero % 2 == 0:
    print(f'O número {numero} é Par')
else:
    print(f'O número {numero} é Impar')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada 
# um dos digitos separados. 
# Ex: digite um número: 1834
# Unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int((input('Informe um número: ')))

num = str(numero)

print(f'Analisando o número {numero}')

print(f'Unidade: {num[3]} ')
print(f'Dezena: {num[2]} ')
print(f'Centena: {num[1]} ')
print(f'Milhar: {num[0]}' )

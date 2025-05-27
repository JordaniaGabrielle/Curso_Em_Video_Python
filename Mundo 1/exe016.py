# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# exemplo: entrada : 6.345 saida: 6

from math import floor

num_real = float(input("Digite um número Real para ver ele inteiro: "))

num_inteiro = floor(num_real)

print(f"O numero {num_real} inteiro é: {num_inteiro}")
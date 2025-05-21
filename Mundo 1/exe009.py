# Faça um programa que leia um número inteiro qualquer e mostre na sua tabuada.

valor = int(input("Digite um número para ver sua tabuada : "))
x = 0

while x < 10:
    x += 1
    resultado = valor * x
    print(f"{valor} x {x} = {resultado}")
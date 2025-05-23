# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$ 3,27

real = float(input("Quanto de Real voce gostaria de trocar por Dolar ? "))

us = 3.27

dolar = (real / us)

print(f"Com {real} voce pode comprar US${dolar}")
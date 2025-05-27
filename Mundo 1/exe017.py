# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo
# calcule e mostre o comprimento da hipotenusa

cateto_oposto = int(input("Digite o cm do cateto oposto: "))

cateto_adjacente = int(input("Digite o cm do cateto adjacente: "))

hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** 0.5

print(f"A Hipotenusa: {hipotenusa}")


# Utilizando a biblioteca Math função Hypot

print(30*"-")

from math import hypot

cateto_oposto = int(input("Digite o cm do cateto oposto: "))

cateto_adjacente = int(input("Digite o cm do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"resposta:{hipotenusa}")
# Faça um programa que leia a laregura e a altura de uma parede em metros
#  calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.

larg = float(input("Largura da parede : "))

alt = float(input("Altura da parede : "))

area = (larg * alt)

print(f"Sua parede tem a dimensão de {larg}x{alt} e {area}m2.")

tinta = area / 2

print("Para pintar essa parede, você precisará de {tinta}l de tinta. ")
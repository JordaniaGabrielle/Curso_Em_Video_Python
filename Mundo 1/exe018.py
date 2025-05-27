# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#  seno casseno e tangente desse ângulo.
import math

angulo = float(input("Digite um ângulo em graus: "))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno de {angulo}°: {seno:.3f}")
print(f"Cosseno de {angulo}°: {cosseno:.3f}")
print(f"Tangente de {angulo}°: {tangente:.3f}")


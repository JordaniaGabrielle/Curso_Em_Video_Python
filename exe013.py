# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o seu salário? "))

aumento = salario * 0.15

nv_salario = salario + aumento

print(f"O aumento em seu salario de: {salario}\n foi de: {aumento}\n totalizando: {nv_salario} ")

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçôes possiveis sobre ele.

algo = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(algo))

print("Só tem espaços? ", algo.isspace())

print("É númerico ? ", algo.isnumeric())

print("É alfabético? ", algo.isalpha())

print("É alfanumérico ?", algo.isalnum())

print("Esta em maiúsculas? ", algo.isupper())

print("Esta em minúsculas", algo.islower())

# isUpperCase / saber é maiusclo  ....  

#isLowerCase #  / saber se é minusculo

# console.log (typeof algo) / saber qual o tipo

# algo.includes(" ") / Identificar se tem espaços
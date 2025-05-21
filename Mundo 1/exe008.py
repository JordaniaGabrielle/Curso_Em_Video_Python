# Escrve um progrma que leia um valor em metros e o exiba convertido em centi´metros e milímetros.

valor = float(input("Digite um valor em metros (m) : "))

cm = valor * 100

mm = valor * 1000

print(f" Metros = {valor}\n Centímetros = {cm}\n Milimetros = {mm}")
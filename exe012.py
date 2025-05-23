# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

total = float(input("Digite o valor do produto: "))

desconto = total * (5 / 100)

novo_valor = total - desconto

print(novo_valor)
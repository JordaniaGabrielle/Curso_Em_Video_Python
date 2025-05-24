# Escreva um programa que pergunte a quantidade de KM percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preco a pagar. Sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

km = float(input("Quantos KM voce percorreu? "))

dia_alugado = int(input("Quantos dias ele ficou alugado? "))

valor_dia = dia_alugado * 60

valor_km = km * 0.15

total = valor_dia + valor_km

print(f"O valor do KM foi {valor_km}R$ e o valor do aluguel do dia de {valor_dia}R$ .. totalizando : {total}")

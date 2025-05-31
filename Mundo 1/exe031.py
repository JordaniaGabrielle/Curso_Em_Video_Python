
# Desenvolva um programa que pergunte a distância de uma viagem em km
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0.45 para viagem mais longas

distancia = float(input('Qual a distância da sua viagem?  '))


if distancia <= 200:
    cobranca = distancia * 0.50
    print(f'foram cobrados 0,50 por km, resultando o valor em {cobranca}R$')
else:
    cobranca = distancia * 0.45
    print(f'foram cobrados 0,45 por km, resultando o valor em {cobranca}R$')

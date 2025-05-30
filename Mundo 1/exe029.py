# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = ((velocidade - 80) * 7)
    print(f'MULTADO! voce ultrapassou 80km .. Voce deve pagar 7R$ por km ultrapassado, resultando {multa}R$ a multa')
else:
    print(f'{velocidade} Velocidade dentro do limite adequado .. Digira com cuidado!')
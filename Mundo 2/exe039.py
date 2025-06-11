# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que faltou ou que passou do prazo
from datetime import datetime

ano_nascimento = int(input('Em qual ano voce nasceu ?  '))

ano_atual = datetime.now().year

idade =  ano_atual - ano_nascimento

if idade < 17:
    anos = 18 - idade
    print(f'Voce ainda vai se alistar em {anos} anos ')
elif idade > 18:
    anos = idade - 18
    print(f'Voce passou do tempo de se alistar, era pra ter se alistado em {anos} atras')
else:
    print('É hora de se alistar')

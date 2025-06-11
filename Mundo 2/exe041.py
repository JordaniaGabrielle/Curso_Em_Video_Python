# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua catergoria
# de acordo com a idade:
# ate 9 anos: MIRIM - ate 14 anos: INFANTIL - ate 19 anos: JUNIOR - ate 25 anos: SENIOR - acima : MASTER

from datetime import datetime

ano_atual = datetime.now().year

ano_nascimento = int(input('Em qual ano voce nasceu? '))

categoria = ano_atual - ano_nascimento

if categoria < 9:
    print('Categoria: MIRIM')
elif categoria < 14:
    print('Categoria: INFANTIL')
elif 
# Crie um programa que leia o nome de uma cidade e diga se ela 
# começa ou não com o nome "Santo"

cidade = input('Em qual cidade voce nasceu ? ')

cidade2 = cidade.upper()

if 'SANTO' in cidade2:
    print('Existe a palavra "Santo" no nome da sua cidade')

else:
    print('Não existe a palavra "Santo" no nome da sua cidade')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

from time import sleep

computador = randint(0, 5)

jogador = int(input('Tente acertar o numero entre 0 e 5 que estou pensando...'))

sleep(1)
print('...Loading...')
sleep(1)

if computador == jogador:
    print(f'Parabens! voce acertou! estava pensando no {computador}')
elif computador != jogador:
    print(f'Ixii! Voce perdeu... Eu estava pensando no número {computador}')
else:
    print('Número invalido.. Digite um numero entre 0 e 5')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos 
# de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre sorteada.

from random import sample

lista = int(input('Quantos alunos vão apresentar? '))

count = 0

participantes = []

while count < lista:
    count += 1
    nomes = input(f'{count}* :')
    participantes.append(nomes)

print(f'A ordem das apresentaçôes dos {count} alunos serão: \n {sample(participantes, k=count)}')



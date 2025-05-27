# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e esquevrendo o nome do escolhido
from random import choice

count = 0
alunos = []

lista = int(input('Quantos alunos vai sortear? '))

while count < lista:
    count += 1

    nome = input(f"Digite o nome do {count}* aluno:  ")
    alunos.append(nome)

print(f'O aluno sorteado: {choice(alunos)}')

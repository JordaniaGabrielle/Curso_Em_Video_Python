# Crie um programa que leia duas notas de um aluno e calcule a sua media, mostrando uma mensagem no final, de acordo com a média atingida:
# mostrando uma mensagem no final, de acordo com a média atingida
# media abaixo de 5.0: reprovado
# media entre 5.0 e 6.9: recuperação
# media 7.0 ou superior: aprovado

n1 = float(input('Digite a primeira nota:  '))

n2 = float(input('Digite a segunda nota:  '))

media = (n1 + n2) / 2

if media >= 7.0:
    print(f'media: {media}\n[APROVADO]')

elif media > 4.9 and media < 6.9:
    print(f'media: {media}\n[RECUPERAÇÃO]')

else:
    print(f'media: {media}\n[REPROVADO]')

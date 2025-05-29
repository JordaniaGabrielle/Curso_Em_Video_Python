# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra ¨A¨
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').upper()

print(f'A letra aparece {frase.count('A')}')

print(f'A primeira letra {'A'} aparece na posição {frase.find('A') + 1}')


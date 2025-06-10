# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 - binarios 2 - octal 3 - hexa

numero = int(input('Digite um número:   '))

opcao = int(input('Digite qual operação deseja fazer:\n[1] Binario\n[2] Octal\n[3] Hexadecimal\n'))

if opcao == 1:
    print(f'O {numero} em Binario é: ', bin(numero) )
elif opcao == 2:
    print(f'O {numero} em Octal é: ', oct(numero) )
elif opcao == 3:
    print(f'O {numero} em Hexadecimal é: ', hex(numero) )
else:
    print('Comando invalido...\n somente opção [1] [2] [3]')
# Faça um programa que leia três números e mostre qual é o maior e qual é o manor.

lista = []
 
while True: 

    numero = input('Digite o número: (Para parar digite "N") ')

    if numero != "N":
        try:
            n = float(numero)
            lista.append(n)

        except ValueError:
            print('Voce deve inserir somente números ')
    else:
        break
    
if lista:
    print('O maior número é: ', max(lista))
    print('O menor número é: ', min(lista))
else:
    print('Nenhum número foi add')


print(lista)

#hot-reload
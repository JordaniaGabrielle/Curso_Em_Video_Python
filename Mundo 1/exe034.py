# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
# Para salários superiores a 1250.00 calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%

salario_funcionario = float(input('Digite o valor do seu salário:  '))

if salario_funcionario <= 1250:
    aumento = salario_funcionario * 0.15
    novo_salario = aumento + salario_funcionario
    print(f'Voce obteve um aumento de 15% ({aumento}) Totalizando: {novo_salario} ')

else:
    aumento = salario_funcionario * 0.10
    novo_salario = aumento + salario_funcionario
    print(f'Voce obteve um aumento de 10% ({aumento}) Totalizando: {novo_salario} ')

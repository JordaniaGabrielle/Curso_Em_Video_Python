# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então então o empréstimo sera negado

valor_casa = float(input('Qual o valor da casa? '))

salario = float(input('Qual o seu salário? '))

quitar = float(input('Em quantos anos vai pagar o total? '))


prestacao =   (valor_casa / ( quitar * 12))

limite = salario * 0.3

if prestacao <= limite:
    print(f'Aprovado voce pagara {prestacao:.2f} de prestação ')
else:
    print(f'Negado, infelizmente compromete mais que 30 % do seu salario')

print(prestacao)



#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor 
#da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 
#30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa: '))
salario = float(input('Seu salario: '))
anos = int(input('Em qtos anos pretende pagar: '))

porcentagem = salario * 0.3 
prestacao = casa / (anos * 12) 

if prestacao < porcentagem:
    print('Aprovado!')
else:
    print('Reprovado')
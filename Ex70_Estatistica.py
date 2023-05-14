'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

nome = preco = soma = maior = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Qual o produto: '))
    preco = float(input('Qual o preço: '))
    cont += 1
    soma += preco
    if preco > 1000:
        maior += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S ou N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{maior} produtos custam mais de R$ 1.000,00') 
print(f'Total gasto na compra R$ {soma}')  
print(f'O produto mais barato é o {barato}')


'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''  

maisde1000 = total = cont = menor = 0
barato = ' '
while True:
    prod = str(input('Produto: '))
    preco = float(input('Preço: R$ '))

    if preco > 1000:
        maisde1000+= 1

    total += preco
    
    cont += 1
    
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = prod

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: [S ou N]')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'{maisde1000} produto(s) custa(m) mais de R$ 1.000,00')
print(f'Total gasto na compra R$ {total}')
print(f'O produto mais barato é o(a) {barato}')

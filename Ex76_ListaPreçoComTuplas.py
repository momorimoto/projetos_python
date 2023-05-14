#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', '1.75',
            'Borracha', '1.00',
            'Caderno', '15.60',
            'Caneta', '3.50',
            'Pasta', '8.00',
            'Mochila', '89.00')
print('-'*41)
print(f'{"LISTAGEM DE PREÇOS":^41}')    #^ quer dizer centralizado entre os 41 caracteres
print('-'*41)

#para cada posicao em range, de zero a len listagem, que quer dizer, de zero a toda listagem
for posicao in range(0, len(listagem)):
#lapis é posicao 0, 1.75 é posição 1 e por ai vai. Item sempre vai ser par e preço impar:
    if posicao % 2 == 0:
#print a posicao par da listagem:
        #print(listagem[posicao])
        
#inclementando o print:
        print(f'{listagem[posicao]:.<30}', end='')  #:.<30 quer dizer 30 espaçamentos preenchidos com pontinhos alinhados a direita
#,end='' quer dizer para o print do preço continuar na mesma linha dos itens
    else:
        print(f'R$ {listagem[posicao]:.>7}')   #:.>7 quer dizer 7 espaçamentos de traz pra frente preenchidos com pontinhos alinhados a esquerda



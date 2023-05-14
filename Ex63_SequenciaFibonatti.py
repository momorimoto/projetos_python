#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos 
#de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

'''n = int(input('Qtos termos vc quer mostrar: '))
#Fibonacci sempre vai começar com ) e 1
termo1 = 0
termo2 = 1
print(f"{termo1} - {termo2}", end=' ')
termo3 = termo1 + termo2
print(f"- {termo3}", end=' ')
#até aqui ele imprimiu o termo 1, 2 e 3. Mas e para dar continuidade?'''

'''n = int(input('Qtos termos vc quer mostrar: '))
#Fibonacci sempre vai começar com ) e 1
termo1 = 0
termo2 = 1
print(f"{termo1} - {termo2}", end=' ')
#vamos criar um while com contador
cont = 3    #começa com 3 pq há temos os 3 primeiros termos
while cont <= n:
    termo3 = termo1 + termo2
    print(f"- {termo3}", end=' ')
#termo1 passa a ser o termo 2
    termo1 = termo2
#termo2 passa a ser o termo3
    termo2 = termo3
#acumula aqui no contador
    cont += 1
print('FIM')'''

'''n = int(input('Digite um número inteiro positivo: \n'))
listaFibonacci = []
a, b = 0,1
cont = 1
while cont <= n:
    listaFibonacci.append(b)
    a, b = b, a+b
    cont += 1
print(listaFibonacci)'''

#O que o append faz (insere um registro após o último elemento, ou seja, ele é útil quando é preciso 
#colocar o novo registro na última posição da tabela.)
#ex = [2,4,6,8,10]
#ex.append(666)
#print(ex)
#[2, 4, 6, 8, 10, 666]

n = int(input('Digite um número inteiro positivo: \n'))
lista = []
a, b = 0,1
cont = 1
while cont <= n:
    lista.append(b)
    a,b = b,a+b
    cont += 1
print(lista)



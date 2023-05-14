#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() 
#e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e 
#a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função 
#anterior.

from time import sleep
from random import randint
numeros = list ()

def sorteia (lista):
    print('Sorteando 5 valores da lista...', end=' ')
    for cont in range (0,5):
        n = randint (1, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print("Pronto!")

def somaPar (lista):
    soma = 0
    lista_par = []
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            lista_par.append(valor)
    print(f'Somando os valores pares da lista {lista_par} temos {soma}')

sorteia (numeros)
somaPar (numeros)

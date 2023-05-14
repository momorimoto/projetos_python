#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#Maneira 1 = importando a biblioteca factorial
from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

#Maneira 2 = executando passo a passo
n = int(input('Digite um numero: '))
c = n
f = 1
while c > 0:
    print(f'{c} ', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')

#Maneira 3 = FOR, considerando que o n é 5
n = int(input('Digite um numero: '))
c = n
f = 1
for c in range (6,0,-1):
    print(f'{c} ', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print(f'{f}')



   



#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
lista = []
resp = 'Ss'
n = 0
soma = 0 
cont = 0 
while resp in 'Ss':
    n = int(input('Numero: '))
    resp = str(input('Quer continuar? [s] [n]'))
    soma += n
    cont += 1
    lista += [n]
media = soma / cont 
print(f'A soma dos numeros é {soma} e a média é {media}')
print(f'O maior numero é', (max(lista)))
print(f'O menor numero é', (min(lista)))






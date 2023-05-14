#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
#para cada jogo, cadastrando tudo em uma lista composta.
import random
num = list(range(1,61))
jogo = []
qtd = int(input('Informe a quantidade de jogos: '))
print('---' * 15)
#A função random.sample() retorna um determinado trecho de uma sequência, e não repete numero.
# Sua sintaxe é: random.sample(sequence, k)
#sequence: representa uma sequência que pode ser uma lista, uma tupla, um range etc.;
#k: indica a quantidade de itens retornados.
for i in range(0,qtd):  #qtde de palpites
  sorteio = random.sample(num, 6)   #6 num aleatorios
  jogo = (sorteio)  
  jogo.sort()   #colocar em ordem crescente
  print(f'Jogo {i + 1:.>15}: {jogo}')


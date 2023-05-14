#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
#jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''import random
computador = random.randint(0,10)
n= 0
while True:
    n = int(input('Digite um numero de 0 a 10; se vc jogar um num par, vc é par, e vice versa: '))
    soma = n + computador
    print(f'Vc jogou {n} e o computador jogou {computador}. Total de {soma}.')
    if soma % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')'''


from random import randint
v=0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P-I]')). strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VC VENCEU!')
            v += 1
        else: 
            print('VC PERDEU, O JOGO ACABOU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VC VENCEU!')
            v += 1
        else:
            print('VC PERDEU, O JOGO ACABOU')
            break




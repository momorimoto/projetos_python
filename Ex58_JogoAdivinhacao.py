#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora 
#o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários 
#para vencer.

'''import random   
computador = random.randint(0,10)    #definindo inicio e fim dos numeros aleatorios
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print(f'Acertou! Foram {palpites} tentativas')'''


'''import random
computador = random.randint(0,10)
acertou = False

while not acertou:
    jogador = int(input('Digite um numero: '))
    if jogador == computador:
        acertou = True
        print('Parabéns, vc acertou!')
    else:
        print('Tente novamente')'''



import random
computador = random.randint(0,10)
acertar = False
while not acertar:
    jogador = int(input('Numero:'))
    if jogador == computador:
        acertar = True
        print('Parabéns!')
    else:
        print('Tente again')














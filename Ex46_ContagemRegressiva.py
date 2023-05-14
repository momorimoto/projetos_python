#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#indo de 10 até 0, com uma pausa de 1 segundos entre eles.

import emoji
from time import sleep
# laço que começa em 10 até 0 (Primeiro -1 é para ele considerar o zero tbm na contagem) 
for cont in range(10, -1, -1): #Segundo -1 é para ele começar de traz pra frente: 10,9,8...
    # imprimindo o contador
    print(cont)
    # pausa de 1 segundos   tomar cuidado com indentação
    sleep(1)
# imprimindo as mensagens 
print(emoji.emojize(':fireworks:')*5)
print(emoji.emojize(':winking_face_with_tongue:', language="alias")*5)
print(emoji.emojize(' :fireworks: :winking_face_with_tongue: ', language="alias")*5) 
print('\033[31mBléééééééé!\033[m')

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(2)
print('********')





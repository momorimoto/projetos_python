#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.

comeca_com = int(input('Primeiro termo: '))
pular_de = int(input('Razao da PA: '))
termo = comeca_com
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo}", end=' ')
        termo += pular_de
        cont += 1
    print('PAUSA')
    mais = int(input('Qtos termos vc quer mostrar a mais: '))
print(f'Projeção finalizada com {total} termos mostrados')



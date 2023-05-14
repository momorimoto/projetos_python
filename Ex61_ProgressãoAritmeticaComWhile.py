#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da 
#progressão usando a estrutura while.

#FOR
'''termo= int(input("Digite um termo: "))      #de onde começa a contar
razao= int(input("Digite a razao: "))       #de qto em qto vai pular
decimo = termo + (10) * razao
#formula para saber o decimo termo de uma PA, ou os 10 primeiros. Se quisesse saber o vigesimo, 
#só trocar pra 20.

for c in range (termo, decimo, razao):
    print(c)    #vai imprimir os 10 primeiros termos'''

#WHILE
comeca_com = int(input('Primeiro termo: '))
pular_de = int(input('Razao da PA: '))
termo = comeca_com
cont = 1
while cont <= 10:
    print(f"{termo}", end=' ')
    termo += pular_de
    cont += 1
print('FIM')

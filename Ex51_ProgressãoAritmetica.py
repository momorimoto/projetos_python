#Desenvolva um programa que leia:
# - o primeiro termo (0) e 
# - a razão (2) de uma PA.   #PA = Progressão Aritmética
# - No final, mostre os 10 primeiros termos dessa progressão.

termo= int(input("Digite um termo: "))      #de onde começa a contar
razao= int(input("Digite a razao: "))       #de qto em qto vai pular
decimo = termo + (10) * razao
#formula para saber o decimo termo de uma PA, ou os 10 primeiros. Se quisesse saber o vigesimo, 
#só trocar pra 20.

for c in range (termo, decimo, razao):
    print(c)    #vai imprimir os 10 primeiros termos


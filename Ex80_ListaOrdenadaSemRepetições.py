#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()
for cont in range (0,5):
    valores.append(int(input("Digite um número:")))
    x = sorted(valores)
print(f'{x}')


'''lista =[]
for cont in range (0,5):
    lista.append(str(input('Nome:')))
    x = sorted(lista)
print(f'{x}')'''


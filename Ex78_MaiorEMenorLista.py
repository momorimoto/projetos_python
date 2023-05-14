#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
#maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()

for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}') 

print(f'O maior número é {max(valores)}')
print(f'O menor número é {min(valores)}')
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
#únicos digitados, em ordem crescente.

lista1 = []
nova_lista_sem_repetidos = []

for cont in range (0,6):
    lista1.append(int(input('Digite um valor: ')))

#colocar na ordem:
    lista1.sort()

#remover repetidos
for elemento in lista1:
    if elemento not in nova_lista_sem_repetidos:
        nova_lista_sem_repetidos.append(elemento)

print(nova_lista_sem_repetidos)
 

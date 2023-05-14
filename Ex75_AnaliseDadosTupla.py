#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#colocando entre parenteses e virgula já estão dentro e uma tupla:
numeros = (int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")))

#imprimir todos os 4 numeros digitados:
print(f'{[numeros]}')

#Qtas vezes aparece o numero 9:
print(f'O número 9 aparece {numeros.count(9)} vez(es)')

#Em que posição o 3 foi digitado:
'''print(f'O número 3 aparece na posição {numeros.index(3)}')'''

#Porém para saber os pares que é a proxima tarefa, vamos ter que fazer diferente:
if 3 in numeros:
    print(f'O numero 3 aparece na posição {numeros.index(3)}')
else:
    print('O 3 não foi digitado nenhuma vez')

#Quais foram os numeros pares:
print(f'Os valores pares são ', end= '')
for n in numeros:
    if n % 2 == 0:
        print(n, end=',')
       


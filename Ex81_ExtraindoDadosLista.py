#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 

lista = []
for numeros in range (0,6):
    lista.append(int(input("Digite um numero: ")))

#A) Quantos números foram digitados.  
print(f'Foram digitados {len(lista)} números')


#B) A lista de valores, ordenada de forma decrescente. 
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')

#C) Se o valor 5 foi digitado e está ou não na lista.
print(f'O 5 aparece {lista.count(5)} vezes na lista')




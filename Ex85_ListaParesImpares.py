#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
#em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

#Lista dentro de outra lista:
num = [[], []]
valor = 0   #contador pq vão ser digitados 7 numeros)

#para o usuario inputar 7x
for c in range (0,7):
    valor = int(input(f"Digite o {c}.o valor: "))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
    
num[0].sort()
num[1].sort()

print(f"Pares: {num[0]}")
print(f"Ìmpares: {num[1]}")
        
                                                                                                                                                              
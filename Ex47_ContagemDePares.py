#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

contador=0
while (contador < 51):
    print(contador)
    contador = contador + 2
#esse fiz sozinha :)

print('~' * 70)

#forma do professor:
#começa a contar do 2 até 51. O ultimo 2 significa que é pra pular de 2 em 2
for n in range (2, 51, 2):  
    print(n, end=' ')

for c in range (0, 51, 2):
    print(c)
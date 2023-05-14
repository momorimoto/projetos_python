#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando 
#um laço for.

n=int(input('Qual tabuada você quer ver? '))
for c in range (0, 11):
    resultado= n * c
    print(f'{n:1} X {c:2} = {resultado}')   #:2 e 1 dentro de {c e n} é para dar espaço
    

n = int(input('Qual tabuada vc quer: '))
for c in range (1, 11):
    total = n * c
    print(f'{n} X {c} = {total}')
#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.  
#B) A soma dos valores da terceira coluna
#C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = somacoluna = 0
#esses for são para colocar os valores digitados nas listas
for l in range (0,3):
    for c in range (0,3):
        #como são 3 linhas e 3 colunas, vai correr 9x para digitar valor
        matriz [l] [c] = int(input('Digite um valor: '))
#esses for são para mostrar a estrutura na tela
for l in range (0,3):
        for c in range (0,3):
            #end='' é para colocar valor um do lado do outro
            print(f'[{matriz[l] [c]}]', end='')    
        
#A) A soma de todos os valores pares digitados. 
            if matriz [l][c] % 2 == 0:
                somapar += matriz [l][c]
        #print com () vazio é para pular linha; e sem essa identação de um recuo sai errado 
        print()
print(f'A soma de todos os números pares é {somapar}')

#B) A soma dos valores da terceira coluna
for l in range(0,3):
    somacoluna += matriz [l][2]
print(f'A soma da terceira coluna é {somacoluna}')

#C) O maior valor da segunda linha
# função max
print(f'O maior valor da segunda linha é {max(matriz[1])}')
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista 
#composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
#possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float (input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append ([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*20)
for indice, aluno in enumerate (ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*40)
    #opc é a numeração do aluno 0,1,2,3
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print("FINALIZANDO")
        break
    if opc <= len (ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha [opc] [1]}')

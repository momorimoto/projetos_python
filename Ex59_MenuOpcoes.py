'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

escolha = 0
while escolha != 5:
    print('''O que você deseja fazer?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Digite (1,2,3,4 ou 5): '))

    if escolha == 1:
        soma = n1 + n2
        print(f'A soma dos números é {soma}')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos números dá {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O {n1} é maior')
        else:
            print(f'O {n2} é maior')
    elif escolha == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Sair')
    

        





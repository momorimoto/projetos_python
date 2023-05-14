# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Numero primo = divisivel apenas 2x (por 1 e por ele mesmo)
# Destacar os numeros primos com cor diferente
# Mostrar quantas vezes ele foi divisivel e se é primo ou não

cont = 0   #aqui para saber qtas vezes o num foi divisivel
x = int(input('Digite um número inteiro: '))
print(f'O numero {x} é divisivel pelos numeros:')
for c in range(1, x +1):    #contador vai do 1 até x(n que usuario digitar e +1 pq o for sempre conta um a menos, é justamente pra ele ir até o num que o usuario digitou)
    if x % c == 0:   #se o numero for divisivel pelo contador
        cont += 1   #aqui para saber qtas vezes o num foi divisivel
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')

print(f'\n\033[37mO numero {x} foi dividido {cont} vezes')   #aqui para saber qtas vezes o num foi divisivel
if cont == 2:
    print('É um número primo')
else:
    print('Não é número primo')


     



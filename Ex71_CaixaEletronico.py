# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário 
#qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor 
#serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('Seja bem vindo ao Banco da Mônica!')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

'''valor = int(input('Digite o valor a ser sacado: '))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor   
print(f'{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota1} notas de 1')'''


'''c = 0
lst = [50, 20, 10, 1]
valor = int(input('Digite o valor para saque: '))
while True:
    if (valor//lst[c]) !=0:
        ced = valor // lst[c]
        print(f'{ced} cédulas de R${lst[c]},00')
        valor = valor % lst[c]
    c += 1
    if c > 3:
        break'''

valor = int(input('Qto vc quer sacar: R$ '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula

        total_cedula += 1

    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break





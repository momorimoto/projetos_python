#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
 
n = int(input("Digite um numero entre 0 e 20: "))

print(f'Vc digitou o numero {extenso[n]}')






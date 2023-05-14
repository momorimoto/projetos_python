#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve 
#mostrar, para cada palavra, quais são as suas vogais.

palavras = ('cachorro', 'gato', 'aves', 'dolar', 'terno', 'cotonete')

for item in palavras:
    print(f'Na palavra {item} temos ')
    for letra in item:
        if letra in 'aeiou':
            print(letra)

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Variáveis globais para somar, contar e armazenar os dados.
somador_idade = 0
contador_mulheres = 0
nome_homem_velho = ''
idade_homem_velho = 0

# Criando o laço de repetição que vai do 1 até o 4.
for dados in range(1, 5):
    # Recebendo o "nome", "sexo" e "idade" das pessoas.
    print('-'*40)

    nome = str(input(f'Digite o nome da {dados}° pessoa: '))
    idade = int(input(f'Digite a idade da {dados}° pessoa: '))
    sexo = str(input(f'Digite o sexo da {dados}° pessoa (m/f): '))
    
    # Criando um somador para somar todas as idades.
    somador_idade += idade

    '''Condição para armazenar o nome e a idade do homem mais velho, dentro do primeiro laço.
    Porém, acredito que esse bloco de código acabe se tornando inútil.
    Porque o bloco de baixo já vai armazenando o nome e a idade através do laço e da variável global.
    if dados == 1 and sexo == 'm':
        nome_homem_velho = nome
        idade_homem_velho = idade'''

    # Agora, caso a próxima idade seja maior que a "idade_homem_velho", as variáveis serão substituídas.
    if sexo == 'm' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome

    # Condição para contar o número de mulheres que tem menos de 20 anos de idade.
    if sexo == 'f' and idade < 20:
        contador_mulheres += 1

# Imprimindo as informações, e realizando o cálculo da média das idades direto no print.
print(f'A média das idades do grupo é de {somador_idade/4:.1f} anos. '
      f'\nO nome do homem mais velho é {nome_homem_velho} com idade {idade_homem_velho} anos.')
print(f'Há {contador_mulheres} mulheres com menos de 20 anos de idade.')







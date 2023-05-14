def jogar ():
    print('***********************')
    print('*****JOGO DA FORCA*****')
    print('***********************')

    palavra_secreta = 'banana' 
    letras_acertadas = ['__', '__', '__', '__', '__', '__',]

#saber se o usuario acertou ou errou: vamos criar duas variaveis boleanas 'enforcou' e 'acertou' para guardar
#essa informação e o jogo continuará até umas delas ser TRUE (para isso criamos um laço while)
    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)
    while (not acertou and not enforcou):

#o usuario vai chutar a letra, se a letra estiver dentro da palavra_secreta, ele acertou. Para isso vamos
#usar um laço FOR:
        chute = input('Qual a letra? ')

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):    #.upper(traz em MAIUSCULA)
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '__' not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print('Você ganhou!')
        else:
            print('Você perdeu')
        print('Fim do Jogo')

#fiz igual do livro e não está funcionando

           



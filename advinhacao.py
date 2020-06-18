import random

def jogar():

    print('*****************************************')
    print('Bem vindo ao nosso programa de advinhação')
    print('*****************************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nivel de dificuldade? ')
    print('(1) Fácil (2) Médio (3) Dificil')
    nivel = int(input('Define o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodadas in range(1, total_de_tentativas+1):
        print('Tetativa: {} de {} '.format(rodadas, total_de_tentativas))
        chute = int(input('Digite um numero entre 1 e 100: '))
        if (chute < 1 or chute > 100):
            print('Você deve digitar um numero entre 1 e 100 ')
            continue

        acertou = (numero_secreto == chute)
        nMaior = chute > numero_secreto
        nMenor = chute < numero_secreto


        if (acertou):
            print('Você acertou, e fez {} pontos!'.format(pontos))
            break
        else:
            if(nMaior):
                print('Você errou! O seu numero foi maior que o numero secreto')
            elif(nMenor):
                print('Você errou! O seu numero foi menor que o numero secreto')
            pontos_perdidos = round(abs(numero_secreto - chute) * 3)
            pontos = pontos - pontos_perdidos


    if(acertou):
        print('Fim do Jogo. Parabens!!')
    else:
        print('Você perdeu. O numero Secreto foi {}'.format(numero_secreto))


if(__name__ == '__main__'):
    jogar()

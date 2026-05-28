import random

pergunta = input('quer jogar zerinho ou um[s/n]:')
while pergunta == 's':
    pri_jogador = int(input('chefinho escolha entre 0 e 1:'))
    seg_jogador = random.randint(0,1)
    ter_jogador = random.randint(0,1)

    if (pri_jogador == 0 and seg_jogador == 1 and ter_jogador == 1) or (pri_jogador == 1 and seg_jogador == 0 and ter_jogador == 0):
        print('valeu, primeiro jogador ganhou')
    elif (seg_jogador == 0 and pri_jogador == 1 and ter_jogador == 1) or (seg_jogador == 1 and pri_jogador == 0 and ter_jogador == 0):
        print('valeu, segundo jogador ganhou')
    elif (ter_jogador == 0 and pri_jogador == 1 and seg_jogador == 1) or (ter_jogador == 1 and pri_jogador == 0 and seg_jogador == 0):
        print('valeu, segundo jogador ganhou')
    else:
        print('é rapaz, deu emapte tecnico')
    pergunta = input('quer jogar zerinho ou um novamente[s/n]:')
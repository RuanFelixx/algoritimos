# Jogo de Dados 7 ou 11
# ➢ Escreva um programa no Python que simule um jogo de dados disputado
# entre um jogador humano e um computador, onde dois dados
# eletrônicos (simulados por software, através de valores aleatórios) devem
# ser lançados simultaneamente. O jogador vence se a soma dos pontos
# dos dois dados for 7 ou 11, caso contrário vence o computador
# ➢ Ao final da partida, o programa deverá perguntar ao usuário se o mesmo
# deseja jogar novamente. O programa deverá permitir uma nova partida,
# caso a resposta seja afirmativa ou encerrar em caso negativo


import random

pontos_jog = 0
pontos_maq = 0
pergunta = input('deseja jogar um jogo de dados[s/n]:')

while pergunta == 's':
    pri_dado = random.randint(1,6)
    seg_dado = random.randint(1,6)
 
    soma = pri_dado + seg_dado

    print('primeiro dado:', pri_dado)
    print('segundo dado:',seg_dado)
    print('soma dos dados:',soma)

    if soma == 7 or soma == 11:
        pontos_jog = pontos_jog +1 
        print('parabens jogador, você ganhou!!!')
    else:
        pontos_maq = pontos_maq + 1
        print('vixeee, vacilão a maquina ganhou kkkkk')

    print('PONTOS DA MAQUINA X PONTOS DO JOGADOR')
    print(f'{pontos_maq} a {pontos_jog}')    
    pergunta = input('deseja jogar novamente[s/n]:')
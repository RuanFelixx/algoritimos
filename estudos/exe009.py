# Pedra, Papel e Tesoura
# ➢ Escreva um programa no Python que simule o jogo PEDRA, PAPEL e
# TESOURA, a ser disputado entre um jogador humano e o computador.
# ➢ O jogador humano deverá escolher entre uma das três opções e a
# escolha do computador deverá ser feita de forma aleatória.
# ➢ O programa deverá realizar o julgamento e definir quem venceu o jogo,
# lembrando que PEDRA vence TESOURA, TESOURA vence PAPEL e PAPEL
# vence PEDRA. Considere a possibilidade de haver empate.
# ➢ O jogador deverá poder jogar novamente, caso deseje
import random

pergunta = input('deseja jogar pedra, papel e tesoura: [s/n]:')
quant_comp = 0
quant_joga = 0
quant_empa = 0
while pergunta == 's':
    comp_jogada = random.randint(1,3) #para o computador 1 vale pedra, 2 papel e 3 tesoura
    escolha_jogador = input('escolha entre pedra papel e tesoura:')

    if (comp_jogada == 1 and escolha_jogador == 'tesoura') or (comp_jogada == 2 and escolha_jogador == 'pedra') or (comp_jogada == 3 and escolha_jogador == 'papel'):
        print('o computador venceu')
        quant_comp = quant_comp + 1
    elif (comp_jogada == 1 and escolha_jogador == 'papel') or (comp_jogada == 2 and escolha_jogador == 'tesoura') or (comp_jogada == 3 and escolha_jogador == 'pedra'):
        print('jogador venceu')
        quant_joga = quant_joga + 1
    else:
        print('opa, empate')
        quant_empa = quant_empa + 1
    print('quantidade de vitorias do computador:',quant_comp)
    print('quantidade de empates:',quant_empa)
    print('quantidade de vitorias do jogador:',quant_joga)
    pergunta = input('deseja jogar novamente[s/n]:')
# Qual o seu vinho preferido?
# Escreva um programa em Python que
# permita entrevistar um grupo de
# pessoas sobre seu tipo de vinho
# preferido
# Cada indivíduo deverá escolher entre
# BRANCO, TINTO ou ROSÉ
# Ao final da entrevista, o programa
# deverá apresentar os resultados da
# pesquisa, indicando quantos votos
# cada uma das opções recebeu

rose = 0 
tinto = 0
branco = 0

q = int(input('quantas pessoas serão intrevistadas:'))

for i in range(0,q):
    vinho_pre = input('caro usuario, qual é seu vinho favorito [branco/tinto/rose]:')
    if vinho_pre == 'rose':
        rose = rose +1 
    elif vinho_pre == 'branco':
        branco = branco + 1
    elif vinho_pre == 'tinto':
        tinto = tinto + 1
    else:
        print('opa chefe, nenhuma das opções')
print(f'''
votos de rose:{rose}
votos do tinto:{tinto}
votos do branco:{branco}
''')
naruto = 0 
goku = 0
tanjiro = 0

q = int(input('quantas pessoas serão intrevistadas:'))

for i in range(0,q):
    print(f'''
    para naruto escolha 1
    para goku escolha 2
    para tanjiro escolha 3
    ''')
    
    personagem_pre = int(input('caro usuario, qual é seu personagem favorito:'))
    if personagem_pre == 1:
        naruto = naruto +1 
    elif personagem_pre == 2:
        tanjiro = tanjiro + 1
    elif personagem_pre == 3:
        goku = goku + 1
    else:
        print('opa chefe, nenhuma das opções')


total = naruto + goku + tanjiro
percnar = naruto / total * 100
percgok = goku / total * 100
perctan = tanjiro / total * 100
print("Foram entrevistadas %d pessoas.\n"%total)

print(f'''
votos para naruto:{naruto}
votos para goku:{goku}
votos para tanjiro:{tanjiro}
''')

print(f'''
percentual para naruto:{percnar}
percentual para goku:{percgok}
percentual para tanjiro:{perctan}
''')
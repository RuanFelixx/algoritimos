# lista = []

# num = int(input('digite quantos valores quer add:'))

# for i in range(0,num):
#     valor = int(input('digite um valor:'))
#     lista.append(valor)


# print(lista)




carros = []

pergunta = input('deseja fazer algo com seus carros[s/n]:')

while pergunta == 's':
    print('''
    Escolha uma das opções abaixo:
    [1] adicionar carro
    [2] pocisão carro 
    [3] remover carro
    [4] listar carro
    [5] editar carro
    ''')
    opcao = int(input('escolha umas das opções:'))
    if opcao == 1:
        carro = input('nome do carro:')
        modelo = input('modelo do carro:')
        placa = input('placa do carro:')
        ano = int(input('ano do carro:'))

        carros.append(carro)
        carros.append(modelo)
        carros.append(placa)
        carros.append(ano)

        print('carro adicionado, com sucesso')

    elif opcao == 2:
        pos_carro = input('nome do carro que deseja saber a pocisão na lista:')
        print(carros.index(pos_carro))

    elif opcao == 3:
        rem_carro = input('nome do carro que deseja remover:')
        if rem_carro in carros:
        
            rem_modelo = input('nome do modelo que deseja remover:')
            rem_placa = input('placa que deseja remover:')
            rem_ano = int(input('ano do carro que deseja remover:'))

            carros.remove(rem_carro)
            carros.remove(rem_modelo)
            carros.remove(rem_placa)
            carros.remove(rem_ano)
        else:
            print('carro não encontrado')

    elif opcao == 4:
        print('lista dos carros:')
        print(carros)

    elif opcao == 5:
        pergunta = input('deseja editar nome, modelo, placa ou ano:')
        if pergunta == 'nome':
            carro_antigo = input('digite o nome do carro que deseja trocar:')
            if carro_antigo in carros:
                novo_nome = input('Novo nome do carro: ')
            
                indice_nome = carros.index(carro_antigo)
                carros[indice_nome] = novo_nome
            else:
                print('não encontrado')

        elif pergunta == 'modelo':
            modelo_antigo = input('o modelo do carro que deseja trocar:')
            if modelo_antigo in carros:
                novo_modelo = input('digite o novo nome do modelo do carro:')

                indice_modelo = carros.index(modelo_antigo)
                carros[indice_modelo] = novo_modelo
            else:
                print('modelo não encontrado')
        elif pergunta == 'placa':
            placa_antiga = input('digite o nome da placa que deseja trocar:')
            if placa_antiga in carros:
                nova_placa = input('novo nome da placa:')

                indice_placa = carros.index(placa_antiga)
                carros[indice_placa] = nova_placa
            else:
                print('placa não encontrado')
        
        elif pergunta == 'ano':
            ano_antigo = int(input('digite o ano do carro que deseja trocar:'))
            if ano_antigo in carros:
                novo_ano = int(input('digite o novo ano:'))

                indice_ano = carros.index(ano_antigo)
                carros[indice_ano] = novo_ano
            else:
                print('ano não encontrado')
        else: 
            print('nenhuma das oções')
        

    pergunta = input('deseja continuar[s/n]:')

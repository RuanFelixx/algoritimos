print('BEM VINDO, AO SISTEMA DE GESTÃO DE CABELEIREIROS !!!')

clientes = []

pergunta = input('Você deseja gerenciar[s/n]:')


while pergunta == 's' or pergunta == 'S':

    print('''
        [1]Gerenciar clientes
        [2]Gerenciar serviços
        [3]Gerenciar agendamentos
        [4]Ver relatorios
        [5]Sobre o sistema
        [6]Sair
    ''')

    opcao = int(input('escolha uma das opções:'))

    if opcao == 1:
        print('''
             [1] Cadastrar cliente
             [2] Remover cliente
             [3] Editar infpormações de cliente
             [4] Listar clientes
        ''')

        opcao = int(input('escolha uma das opções:'))

        if opcao == 1:
            nome_cliente = input('digite o nome do cliente:')
            cpf_cliente = input('didte o cpf do cliente:')
            celular_cliente = input('digite o numero do celular do cliente:')
            email_cliente = input('digite o email do cliente:')

            print('Cadastrado com sucesso!!!') #ta mentindo sim, pelo menos por enquanto

    elif opcao == 2:
        print()

    elif opcao == 3:
        print()
    
    elif opcao == 4:
        print()
    
    elif opcao == 5:
        print()

    elif opcao == 6:
        print()
    
    else:
        print('Nenhuma das opções!!!')
    
    pergunta = input('Você deseja gerenciar[s/n]:')

   
#sistema de gestão para cabeleireiros
#1 crud para clientes (modulos)
#2 crud para servios (modulos)
#3 crud para agendamentos (modulos)
#4 modulo relatorios 
#5 modulo sobre o sistema 
#6 sair



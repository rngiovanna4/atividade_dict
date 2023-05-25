agenda = {}

#Menu de opções
def menu():
    print('-'*40)
    print(' '*14,'AGENDA')
    print('-'*40)

    print(' '*14,'MENU')
    print("""Selecione uma das opções abaixo:
    1 - Cadastrar
    2 - Editar 
    3 - Excluir
    4 - Pesquisar contato
    5 - Classificar por ordem de cadastro dos contatos 
    6 - Classificar por ordem alfabética
    7 - Sair do programa""")
    opcao = opcao_escolhida()
    return opcao

# Verificar se o usuário digitou uma opção válida
def opcao_escolhida():
    opcao = (input('Digite a opção escolhida: '))
    if (opcao.isnumeric==False):
        print('Opção inválida.')
        opcao = input('Digite uma opção válida: ')
    else:
        while(int(opcao)>7 or int(opcao)<0):
            print('Opção inválida.')
            opcao = input('Digite uma opção válida: ')


        #opcao = int(opcao)
    #return opcao

#Continuar ou encerrar?
def continuar():
    y_or_n = input('Digite 1 para abrir menu ou 2 para encerrar: ')

    while (y_or_n != '1' and y_or_n != '2'):
        print('Opção inválida.')
        y_or_n = input('Digite uma opção válida: ')
    else:
        if y_or_n == '1':
            opcao = menu()
        elif y_or_n == '2':
           opcao = 7
    return opcao


#Cadastrar, pelo menos, 5 contatos.
def cadastrar_contatos():
    for i in range(3):
        nome = input('Digite o nome do {}º contato\n'.format(i+1))
        num = input('Digite o número de contato\n')
        agenda [nome] = num
        print ('Contato de {} salvo com sucesso'.format(nome))
    print(agenda)
    opcao = continuar ()
    return opcao
    

#Editar contatos
def editar():
    nome = input('Digite o nome do contato que deseja editar ')
    n_or_c= input("""Esolha uma das opções: 
    1 - Editar número
    2 - Editar  nome """)

    #Verificar a opção digitada
    while (n_or_c != '1' and n_or_c != '2'):
        print('Opção inválida.')
        n_or_c = input('Digite uma opção válida: ')
    else:
        if n_or_c == '1':
            #Edita o número, o valor da chave
            num = input('Digite o novo número ')
            agenda.update({nome:num})
            print('Numero alterado com sucesso')
            print(agenda)
        else:
            #"Edita" o nome, a chave do dicionário
            novonome = input('Digite o novo nome ')
            agenda[novonome] = agenda[nome]
            del agenda[nome]
        print('Nome alterado com sucesso')
        print(agenda)
    opcao = continuar ()
    return opcao
     

#Excluir contatos
def excluir():
    nome = input('Digite o nome do contato que deseja excluir ')
    del agenda[nome]
    print('Contato excluido com sucesso')
    print(agenda)

    opcao = continuar ()
    return opcao

#Pesquisar contato pelo nome
def pesquisar():
    nome = input('Digite o nome do contato que deseja pesquisar ')
    print(agenda.get(nome, 'Nome não encontrado\n'))

    opcao = continuar ()
    return opcao
#Classificar por ordem de cadastro
def ordemdecadastro():
    print(agenda)

    opcao = continuar ()
    return opcao

#Classificar por ordem do nome dos contatos
def ordemalfabetica():
    ordalf = sorted(agenda)
    print(ordalf)

    opcao = continuar ()
    return opcao

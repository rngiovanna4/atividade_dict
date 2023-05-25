import funcoesagenda

opcao = funcoesagenda.menu()

while (opcao < 7 and opcao>0):
    if opcao == 1:
        opcao = funcoesagenda.cadastrar_contatos()
    elif opcao == 2:
        opcao = funcoesagenda.editar()
    elif opcao == 3:
        opcao = funcoesagenda.excluir()
    elif opcao == 4:
        opcao = funcoesagenda.pesquisar() 
    elif opcao == 5:
        opcao == funcoesagenda.ordemdecadastro()
    elif opcao == 6:
        opcao == funcoesagenda.ordemalfabetica()     
else:
    print("O menu foi encerrado com sucesso ")



def desafio1rocketseat():
    lista_contatos = []

    print("Desafio 1 - Rocketseat")

    while True:
        print("Selecione uma das funções abaixo:")

        print("[1] - Adicionar um novo contato")
        print("[2] - Visualizar lista de contatos")
        print("[3] - Editar um contato")
        print("[4] - Favoritar/Desfavoritar um contato")
        print("[5] - Lista de contatos favoritos")
        print("[5] - Deletar um contato")
        print("[6] - Sair")

        opcao_selecionada = int(input("Digite a opção desejada: "))

        if opcao_selecionada == 1:
            novo_contato = adicionar_novo_contato()
            lista_contatos.append(novo_contato)
        elif opcao_selecionada == 2:
            show_lista_contatos(lista_contatos)
        elif opcao_selecionada == 6:
            break



def adicionar_novo_contato():
    print("Digite os dados do usuário:")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito (S/N): ")
    print("Contato adicionado com sucesso!")

    return {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': favorito}

def show_lista_contatos(lista_contatos):
    if len(lista_contatos) == 0:
        print("Nenhum contato cadastrado.")
    else:
        print(lista_contatos)

desafio1rocketseat()
def atualizar():
    receitas = open("./data/receitas.csv", "r")

    nome = input('Digite a receita que você deseja atualizar: ')

    for receita in receitas:
        if receita['Nome'] == nome:
            atualizacao = input(
                'O que você deseja atualizar? Nome [N], País [P], Ingredientes [I], Modo de Preparo [M], Favorito [F]: ')

    receitas.close()

def atualizar():
    file=open("./data/receitas.csv", "r")

    for linha in file:
        print(linha)

        
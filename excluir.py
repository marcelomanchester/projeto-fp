def excluir():
    file = open("./data/receitas.csv", "r")

    apagar = input('Digite o nome da receita que você deseja excluir: ')

    for line in file:
        print(line)
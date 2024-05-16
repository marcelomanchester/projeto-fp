def excluir():
    file = open("./data/receitas.csv", "r")
    lines=file.readlines()

    apagar = input('Digite o nome da receita que você deseja excluir: ')

    for line in lines:
        if apagar in line:
            file.pop(line)

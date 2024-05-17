def excluir():
    file = open('./data/receitas.csv', 'r')
    lines = file.readlines()

    apagar = input('Digite o nome da receita que você deseja excluir: ')
    index_deletar = -1

    for index, line in enumerate(lines):
        receita = line.split(',')

        if apagar == receita[0]:
            index_deletar = index

    if index_deletar == -1:
        print('Receita não encontrada')
    else:
        lines.pop(index_deletar)

    file.close()

    file2 = open('./data/receitas.csv', 'w')
    file2.writelines(lines)
    file2.close()

def excluir():
    file = open('./data/receitas.csv', 'r', encoding='utf8')
    lines = file.readlines()

    while True:
        cont = 0
        nome = input(
            'Digite o nome da receita que você deseja excluir ou [0] para voltar ao menu principal: ')

        if nome == '0':
            break
        else:
            index_deletar = -1

            for index, line in enumerate(lines):
                receita = line.split('@')

                if nome == receita[0]:
                    index_deletar = index

            if index_deletar == -1:
                while True:
                    erro = input(
                        'Receita não encontrada! Digitar outra receita [1], voltar ao menu principal [0]:')

                    if erro == '1':
                        break
                    elif erro == '0':
                        cont += 1
                        break
                    else:
                        print('Caractere inválido!')
                        continue
            else:
                lines.pop(index_deletar)
                print('Receita excluída!')

            if cont != 0:
                break

    file.close()

    file2 = open('./data/receitas.csv', 'w', encoding='utf8')
    file2.writelines(lines)
    file2.close()

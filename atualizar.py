def atualizar_ingredientes():
    ingredientes = []

    while True:
        ingredientes.append(input(
            'Digite os novos ingredientes ou [B] finalizar: '))

        if ingredientes[-1] == 'B':
            ingredientes.pop()
            break

    return ';'.join(ingredientes)


def atualizar_preparo():
    preparo = []

    while True:
        preparo.append(input(
            'Digite o novo modo de preparo ou [B] finalizar: '))

        if preparo[-1] == 'B':
            preparo.pop()
            break

    return ';'.join(preparo)


def atualizacao(receita):
    while True:
        atualizacao = input(
            'O que você deseja atualizar? Nome [N], País [P], Ingredientes [I], Modo de Preparo [M], Favorito [F] ou Finalizar atualização [B]: ').upper()

        if atualizacao == 'N' or atualizacao == 'P' or atualizacao == 'I' or atualizacao == 'M' or atualizacao == 'F' or atualizacao == 'B':
            if atualizacao == 'B':
                break
            elif atualizacao == 'N':
                novo_nome = input('Substituição: ')
                receita[0] = novo_nome
            elif atualizacao == 'P':
                novo_pais = input('Substituição: ')
                receita[1] = novo_pais
            elif atualizacao == 'I':
                novo_ingrediente = atualizar_ingredientes()
                receita[2] = novo_ingrediente
            elif atualizacao == 'M':
                novo_preparo = atualizar_preparo()
                receita[3] = novo_preparo
            elif atualizacao == 'F':
                while True:
                    novo_favorito = input('Favoritos? [S] ou [N]: ').upper()

                    if novo_favorito == 'S' or novo_favorito == 'N':
                        if novo_favorito == 'S':
                            receita[4] = True
                            break
                        else:
                            receita[4] = False
                            break
                    else:
                        print('Caractere inválido')
        else:
            print('Caractere inválido')

    return f'{receita[0]}, {receita[1]}, {receita[2]}, {receita[3]}, {receita[4]}\n'


def atualizar():
    file = open("./data/receitas.csv", "r")
    receitas = file.readlines()

    cont = 0

    while True:

        nome = input('Digite a receita que você deseja atualizar: ')

        for index, receita in enumerate(receitas):
            receita_array = receita.split(',')

            if receita_array[0] == nome:
                receita_atualizada = atualizacao(receita_array)
                receitas[index] = receita_atualizada
                file.close()

                file = open("./data/receitas.csv", "w")
                file.writelines(receitas)
                file.close()

                cont = 0
                break
            else:
                cont += 1

        if cont != 0:
            print('Digite uma receita válida!')
            continue
        else:
            break

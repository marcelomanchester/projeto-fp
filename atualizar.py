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
                novo_ingrediente = input('Substituição: ')
                receita[2] = novo_ingrediente
            elif atualizacao == 'M':
                novo_preparo = input('Substituição: ')
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
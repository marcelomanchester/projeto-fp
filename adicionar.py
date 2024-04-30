def adicionar():
    receita = {
        'Nome': '',
        'País': '',
        'Ingredientes': [],
        'Modo de preparo': [],
        'Favorito': False
    }

    instrucoes = []

    receita = input('Nome da receita: ')
    pais = input('País de origem: ')

    instrucoes.append('Ingredientes: ')

    while True:
        instrucoes.append(input(
            'Digite os ingredientes ou [0] para começar a escrever o modo de preparo: '))

        if instrucoes[-1] == '0':
            instrucoes.pop()
            break

    instrucoes.append('Modo de preparo: ')

    while True:
        instrucoes.append(
            input('Digite o modo de preparo ou [0] para finalizar: '))

        if instrucoes[-1] == '0':
            instrucoes.pop()
            break

    favorito = input('Deseja adicionar aos favoritos? [S] ou [N]? ').upper()

    if favorito == 'S':
        favoritos[receita] = [instrucoes]

    receitas[receita] = [instrucoes]
    paises[pais] = [receita]

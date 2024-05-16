def gerar_receita():
    return {
        'Nome': '',
        'País': '',
        'Ingredientes': [],
        'Modo de preparo': [],
        'Favorito': False
    }


def add_ingrediente(receita):
    while True:
        receita['Ingredientes'].append(input(
            'Digite os ingredientes ou [0] para começar a escrever o modo de preparo: '))

        if receita['Ingredientes'][-1] == '0':
            receita['Ingredientes'].pop()
            break

    return receita


def add_modo_de_preparo(receita):
    while True:
        receita['Modo de preparo'].append(
            input('Digite o modo de preparo ou [0] para finalizar: '))

        if receita['Modo de preparo'][-1] == '0':
            receita['Modo de preparo'].pop()
            break

    return receita


def add_favorito(receita):
    while True:
        try:
            favorito = input('Deseja adicionar aos favoritos? [S] ou [N]? ').upper()
            receita['Favorito'] = (favorito == 'S')
            return receita
            break
        except ValueError:
            print()


def salvar(receita):
    with open("./data/receitas.csv", "a") as file:
        file.write(f'{receita["Nome"]}, {receita["País"]}, {";".join(receita["Ingredientes"])}, {";".join(receita["Modo de preparo"])}, {receita["Favorito"]}\n')


def adicionar():
    receita = gerar_receita()
    receita['Nome'] = input('Nome da receita: ')
    receita['País'] = input('País de origem: ')
    receita = add_ingrediente(receita)
    receita = add_modo_de_preparo(receita)
    receita = add_favorito(receita)
    salvar(receita)
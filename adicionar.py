def gerar_receita():
    return {
        'Nome': '',
        'País': '',
        'Ingredientes': [],
        'Modo de preparo': [],
        'Favorito': False,
        'Avaliação': 0
    }


def validar_input(receita, chave, mensagem_input):
    while True:
        nome = input(mensagem_input).strip()

        if nome != '':
            receita[chave] = nome
            break
        else:
            print(f'Digite um {chave} válido!')


def add_list_item(receita, chave, mensagem_input, mensagem_erro):
    while True:
        item = input(mensagem_input).strip()

        if item == '0':
            break
        elif item != '':
            receita[chave].append(item)
        else:
            print(mensagem_erro)

    return receita


def add_favorito(receita):
    while True:
        favorito = input(
            'Deseja adicionar aos favoritos? [S] ou [N]? ').upper()

        if favorito == 'S':
            receita['Favorito'] = (favorito == 'S')
            break
        elif favorito == 'N':
            receita['Favorito'] = (favorito == 'S')
            break
        elif favorito != 'S' and favorito != 'N':
            print('Digite um caracter válido!')
            continue

    return receita


def salvar(receita):
    with open('./data/receitas.csv', 'a', encoding='utf8') as file:
        file.write(f'{receita['Nome']}@{receita['País']}@{';'.join(receita['Ingredientes'])}@{
                   ';'.join(receita['Modo de preparo'])}@{receita['Favorito']}@{receita['Avaliação']}\n')


def adicionar():
    receita = gerar_receita()

    validar_input(receita, 'Nome', 'Digite o nome: ')
    validar_input(receita, 'País', 'Digite o país: ')

    receita = add_list_item(
        receita, 'Ingredientes', 'Digite um ingrediente ou [0] para finalizar: ', 'Digite um ingrediente válido!')
    receita = add_list_item(receita, 'Modo de preparo',
                            'Digite o modo de preparo ou [0] para finalizar: ', 'Digite um modo de preparo válido!')
    
    receita = add_favorito(receita)
    salvar(receita)

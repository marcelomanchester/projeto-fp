import adicionar


def set_receita(lista):
    cont = 0
    receita = adicionar.gerar_receita()

    for key in receita.keys():
        receita[key] = lista[cont]
        cont += 1

    return receita


def set_filter():
    option = input(
        'Digite como você deseja visualizar:\n 0 - Voltar ao menu \n 1 - Todos\n 2 - Filtrar por país\n 3 - Mostrar favoritos\n')

    if option == '0':
        return 'EXIT', ''
    elif option == '1':
        return 'ALL', ''
    elif option == '2':
        country = input('Informe o nome do país que voce deseja filtrar:\n')
        return 'COUNTRY', country
    elif option == '3':
        return 'FAVORITES', ''


def descrever(receitas):
    name = input('Digite o nome da receita que voce quer visualizar:\n')
    count = 0
    receita = ''

    while count < len(receitas):
        if receitas[count]['Nome'].strip() == name.strip():
            receita = receitas[count]
            break

        count += 1

    if receita == '':
        print('\nReceita nao encontrada.\n')
    else:
        for key in receita.keys():
            output = f' {key}: \n'

            for item in receita[key].split(';'):
                output += f' - {item.strip()}\n'

            print(output)


def filtrar_receita(filter_type, filter):
    receitas = []

    with open('./data/receitas.csv', 'r') as file:
        lista = file.readlines()

    for linha in lista:
        lista = linha.split(',')
        print('Receitas filtradas:')

        if (filter_type == 'COUNTRY' and lista[1].strip() == filter.strip()) or (filter_type == 'FAVORITES' and lista[4].strip() == 'True') or (filter_type == 'ALL'):
            print(f' -  {lista[0]}')
            receitas.append(set_receita(lista))

    return receitas


def visualizar():
    while True:
        filter_type, filter = set_filter()

        if filter_type == 'EXIT':
            break

        receitas = filtrar_receita(filter_type, filter)
        descrever(receitas)

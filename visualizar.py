import adicionar
import os
import platform

def set_receita(lista):
    cont = 0
    receita = adicionar.gerar_receita()

    for key in receita.keys():
        receita[key] = lista[cont]
        cont += 1

    return receita


def skip():
    print('Digite um valor válido!')
    return 'RESTART', ''

def clear():
    sys = platform.system()

    if sys == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


def set_filter():
    try:
        option = int(input(
            'Digite como você deseja visualizar:\n 0 - Voltar ao menu \n 1 - Todos\n 2 - Filtrar por país\n 3 - Mostrar favoritos\n 4 - Filtrar por avaliação\n'))
    
        if not option:
            raise ValueError
        elif option == 0:
            return 'EXIT', ''
        elif option == 1:
            return 'ALL', ''
        elif option == 2:
            country = input('Informe o nome do país que voce deseja filtrar:\n')
            return 'COUNTRY', country
        elif option == 3:
            return 'FAVORITES', ''
        elif option == 4:
            ranking = input(
                'Informe o nível de avaliação que voce deseja filtrar:\n 1 - * \n 2 - ** \n 3 - *** \n 4 - **** \n 5 - *****\n')
            return 'RANKING', ranking
        else:
            raise ValueError
    except ValueError:
        clear()
        return skip()

def descrever(receitas):
    name = input('Digite o nome da receita que voce quer visualizar:\n')
    count = 0
    receita = None

    while count < len(receitas):
        if receitas[count]['Nome'].strip() == name.strip():
            receita = receitas[count]
            break

        count += 1

    if receita == None:
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
            if linha == '\n':
                continue

            lista = linha.split('@')

            if (filter_type == 'COUNTRY' and lista[1].strip() == filter.strip()) or (filter_type == 'FAVORITES' and lista[4].strip() == 'True') or (filter_type == 'ALL') or (filter_type == 'RANKING' and lista[5].strip() == filter):
                print(f' -  {lista[0]}')
                receitas.append(set_receita(lista))

    return receitas


def visualizar():
    while True:
        filter_type, filter = set_filter()

        if filter_type == 'EXIT':
            break

        if filter_type == 'RESTART':
            continue

        receitas = filtrar_receita(filter_type, filter)
        
        if len(receitas) == 0:
            print('Nenhuma receita foi encontrada!')
            continue

        descrever(receitas)

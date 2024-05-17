import random


def index_aleatorio():
    index = []
    cont = 0

    file = open('./data/sugestoes.csv', 'r', encoding='utf8')
    sugestoes = file.readlines()

    for sugestao in sugestoes:
        index.append(cont)
        cont += 1

    i = random.choice(index)

    file.close()

    return i


def receita_aleatoria():

    file = open('./data/sugestoes.csv', 'r', encoding='utf8')
    sugestoes = file.readlines()

    receita_escolhida = sugestoes[index_aleatorio()]

    file.close()

    return receita_escolhida


def adicionar(receita):
    file = open('./data/receitas.csv', 'a', encoding='utf8')
    file.write(receita)
    file.close()


def favorita(receita):
    receita_lista = receita.split('@')

    receita_lista[4] = 'True'

    file = open('./data/receitas.csv', 'a', encoding='utf8')
    file.write('@'.join(receita_lista))
    file.close()


def sugestao():
    receita = receita_aleatoria()
    sugestao = receita.split('@')

    ingredientes = sugestao[2].split(';')
    preparos = sugestao[3].split(';')

    print(sugestao[0])
    print(sugestao[1], '\n')
    print('Ingredientes:\n')

    for ingrediente in ingredientes:
        print(ingrediente)

    print('\n Modo de preparo:\n')

    for preparo in preparos:
        print(f'- {preparo}')

    while True:
        add = input('Você deseja adicionar essa receita? [S] ou [N]: ').upper()

        if add != 'S' and add != 'N':
            print('Digite um caractere válido!')
        elif add == 'S':
            while True:
                fav = input(
                    'Você deseja adicionar aos favoritos? [S] ou [N]: ').upper()

                if fav != 'S' and fav != 'N':
                    print('Digite um caractere válido!')
                elif fav == 'S':
                    favorita(receita)
                    break
                elif fav == 'N':
                    adicionar(receita)
                    break

            break
        elif add == 'N':
            break

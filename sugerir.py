import random


def aleatorio():
    index = []
    cont = 0
    
    file = open('./data/sugestoes.csv', 'r')
    sugestoes = file.readlines()

    for sugestao in sugestoes:
        index.append(cont)
        cont += 1

    receita_sugerida = random.choice(index)

    file.close()

    return receita_sugerida


def receita(receita_sugerida):
    file = open('./data/sugestoes.csv', 'r')
    sugestoes = file.readlines()

    receita_escolhida = sugestoes[receita_sugerida]

    file.close()

    return receita_escolhida


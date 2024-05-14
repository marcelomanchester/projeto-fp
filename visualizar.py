import adicionar


def set_receita(lista):
    cont = 0
    receita = adicionar.gerar_receita()
    for key in receita.keys():
        receita[key] = lista[cont]
        cont += 1
    print(receita)
    return receita


def visualizar():
    while True:
        receitas = []
        
        with open("./data/receitas.csv", "r") as file:
            lista = file.readlines()
        for linha in lista:
            lista = linha.split(',')
            receitas.append(set_receita(lista))
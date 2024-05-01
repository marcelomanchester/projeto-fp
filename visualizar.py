def visualizar():
    while True:
        resposta=input('Deseja ver as receitas: se sim [s] se não [n]: ').lower()
        if resposta=='s':
            with open("./data/receitas.csv", "r") as file:
                lista=file.readlines()
            for itens in lista:
                print(f'{itens}\t')
        else:
            break


def visualizar():

            with open("./data/receitas.csv", "r") as file:
                lista=file.readlines()
            for itens in lista:
                print(f'{itens}\t')
    
        

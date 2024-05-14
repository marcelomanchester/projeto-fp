import adicionar
def visualizar():
    while True:
        resposta=input('Deseja ver as receitas: se sim [s] se não [n]: ').lower()
        receitas = []
        if resposta=='s':
            with open("./data/receitas.csv", "r") as file:
                lista=file.readlines()
            for linha in lista:
                lista = linha.split(',' )
                receitas.append(set_receita(lista))          
        else:
            break
        
        

def set_receita(lista):
    cont=0
    receita=adicionar.gerar_receita()
    for key in receita.keys():
        receita[key]=lista[cont]
        cont+=1
    print(receita)
    return receita      





        

        




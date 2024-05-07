def visualizar():
    resposta=input('você deseja visualizar essa planilha: ')
    if resposta=='s':
        file=open("./data/receitas.csv",'r')
        print(file.read())
        file.close()
        resposta=input('pressione qualquer tecla para sair ')
    else:
        print('')
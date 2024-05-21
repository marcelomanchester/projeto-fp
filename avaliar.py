def estrelas(receita):
    while True:
        try:
            while True:
                estrelas = int(input('Quantas estrelas (1 a 5): '))

                if estrelas != 1 and estrelas != 2 and estrelas != 3 and estrelas != 4 and estrelas != 5:
                    print('Digite um valor válido!')
                    continue
                else:
                    receita[5] = estrelas
                    break

            break
        except ValueError:
            print('Digite um valor válido!')

    return f'{receita[0]}@ {receita[1]}@ {receita[2]}@ {receita[3]}@ {receita[4]}@ {receita[5]}\n'


def avaliacao():
    file = open('./data/receitas.csv', 'r', encoding='utf8')
    receitas = file.readlines()

    cont = 0

    while True:

        nome = input('Digite a receita que você deseja avaliar: ')

        for index, receita in enumerate(receitas):
            receita_lista = receita.split('@')

            if receita_lista[0] == nome:
                receita_avaliada = estrelas(receita_lista)
                receitas[index] = receita_avaliada
                file.close()

                file = open('./data/receitas.csv', 'w', encoding='utf8')
                file.writelines(receitas)
                file.close()

                cont = 0
                break
            else:
                cont += 1

        if cont != 0:
            print('Digite uma receita válida!')
            continue
        else:
            break

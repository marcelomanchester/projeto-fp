import os
import platform
import adicionar
import visualizar
import atualizar
import excluir
import sugerir


def clear():
    sys = platform.system()
    if sys == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


while True:

    # clear()

    print('''
    MENU
    0 - Sair
    1 - Adicionar
    2 - Visualizar
    3 - Atualizar
    4 - Excluir
    5 - Sugerir
  ''')

    try:
        acao = int(input('Bem-vindo Rafael! Digite o que deseja: '))

        # clear()

        if acao == 0:
            break
        elif acao == 1:
            adicionar.adicionar()
        elif acao == 2:
            visualizar.visualizar()
        elif acao == 3:
            atualizar.atualizar()
        elif acao == 4:
            excluir.excluir()
        elif acao == 5:
            sugerir.()

    except ValueError:
        print()

import os
import platform
import adicionar
import visualizar
import atualizar
import excluir
import sugerir
import avaliar


def clear():
    sys = platform.system()

    if sys == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


while True:
    print('''
    MENU
    0 - Sair
    1 - Adicionar
    2 - Visualizar
    3 - Atualizar
    4 - Excluir
    5 - Sugerir
    6 - Avaliar
  ''')

    try:
        acao = int(input('Bem-vindo! Digite o que deseja: '))

        if acao == 0:
            break
        elif acao == 1:
            adicionar.adicionar()
            clear()
        elif acao == 2:
            visualizar.visualizar()
            clear()
        elif acao == 3:
            atualizar.atualizar()
            clear()
        elif acao == 4:
            excluir.excluir()
            clear()
        elif acao == 5:
            sugerir.sugestao()
            clear()
        elif acao == 6:
            avaliar.avaliacao()
            clear()
        else:
            raise ValueError

    except ValueError:
        clear()
        print('Informe um valor válido!')
    except KeyboardInterrupt:
        print('\nAté logo!\n')
        break

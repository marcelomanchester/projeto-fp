import os
import adicionar
import visualizar
import atualizar
import excluir

while True:
  os.system('cls')
  
  print('''
      MENU
      0 - Sair
      1 - Adicionar
      2 - Visualizar
      3 - Atualizar
      4 - Excluir
      5 - Sugerir
  ''')

  acao = int(input('Bem-vindo Rafael! Digite o que deseja: '))

  os.system('cls')

  if acao == 0:
    break
  elif acao == 1:
    adicionar.adicionar()
  elif acao == 2:
    visualizar.visualizar()
    print('')
  elif acao == 3:
    print('')
  elif acao == 4:
    print('')
  elif acao == 5:
    print('')
  else:
    print('Número inválido.')

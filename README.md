# Sistema de Gerenciamento de Receitas

## Índice

1. [Descrição]
2. [Configuração]
3. [Adicionar]
4. [Visualizar]
5. [Atualizar]
6. [Excluir]
7. [Sugerir]
8. [Avaliar]

## 1. Descrição

Este é um sistema de gerenciamento de receitas que permite o usuário adicionar, visualizar, atualizar e exlcuir receitas através de um menu interativo.

Além disso o sistema sugere receitas aleatórias e tem uma funcionalidade que permite o usuário avaliar suas receitas.

## 2. Configuração

### Requisitos:

1. Python 3 instalado.
2. Git CLI instalado.

### Passo a passo:

1. Clone o repositório na sua máquina local. `git clone https://github.com/marcelomanchester/projeto-fp.git`
2. Na pasta raiz do sistema, execute o arquivo main.py: `python main.py`

## 3. Adicionar

O sistema permite que o usuário cadastre informações sobre cada receita, incluindo nome, país de origem, ingredientes e modo de preparo.

Dentro do menu principal ao digitar 1 é possível adicionar uma receita ao seu banco de dados, ao inserir todos os dados a cima, a receita fica disponível para visualizar no menu visualizar.

## 4. Visualizar

O sistema permite que o usuário visualize todas as receitas cadastradas, digitando 2 no menu principal.

Filtragem por país: o sistema permite a visualização das receitas de acordo com o país de origem, facilitando a busca por culinárias específicas.

Filtragem por favoritos: o sistema permite a visualização das receitas marcadas como favoritas.

Filtragem por avaliação: o sistema permite a visualização das receitas de acordo com a sua avaliação dada, entre 1 a 5 estrelas. Facilitando que o usuário encontre as receitas que mais gostou de forma mais rápida.

## 5. Atualizar

O sistema permite que o usuário atualize suas receitas, digitando 3 no menu principal. Ao digitar 3, é solicitado que o usuário diga qual parte da receita ele deseja atualizar (nome, país, ingredientes, modo de preparo ou favoritos).

Ao atualizar, a receita atualizada já fica disponível no menu Visualizar para ser visualizada.

## 6. Excluir

O sistema conta com a funcionalidade de excluir uma receita caso o usuário deseje. No menu ao digitar 4, é perguntado ao usuário qual receita ele deseja excluir, ao digitar o nome, o sistema automaticamente apaga a receita do banco de dados e ela não fica mais disponível para ser visualizada.

## 7. Sugerir

O sistema também conta com uma funcionalidade de sugestão de receitas aleatórias de diferentes países, incentivando o usuário a
experimentar novos pratos.

Ao digitar 5 no menu principal o sistema sugere uma receita aleatória, que após sua leitura é possível adicioná-la a sua lista de receitas e adicioná-la ou não também a sua lista de favoritos.

## 8. Avaliar

Também é possível avaliar suas receitas digitando 6 no menu principal.

Ao digitar 6 é perguntado qual receita o usuário deseja atualizar, basta digitar o nome da receita e depois dar sua nota. Com isso, é possível visualizar as receitas por nota no menu Visualizar.
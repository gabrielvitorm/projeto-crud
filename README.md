## Projeto de Gestão de Aulas e Eventos

Este é um projeto simples de gestão de aulas e eventos desenvolvido com Flask. O projeto utiliza Blueprints para organização do código e armazena os dados em arquivos de texto.

## Funcionalidades

Visualizar, criar, atualizar e deletar aulas
Visualizar, criar, atualizar e deletar eventos

## Intruções para Instalar o Flask

# Crie um ambiente virtual e ative-o:

python -m venv venv
use .\venv\Scripts\activate

# Instale as dependências:

pip install flask

# Estrutura do Projeto
- app.py: Arquivo principal que inicializa a aplicação Flask e registra os Blueprints.
- blueprints/aula.py: Blueprint responsável pelas rotas relacionadas às aulas.
- blueprints/evento.py: Blueprint responsável pelas rotas relacionadas aos eventos.
- blueprints/home.py: Blueprint responsável pelas rotas da página home.
- templates/: Diretório contendo os arquivos HTML.
- static/: Diretório contendo arquivos estáticos como CSS.
- data/: Diretório contendo os arquivos de texto que armazenam os dados das aulas e eventos.

## Estrutura dos Arquivos de Dados
- aulas.txt: Armazena os dados das aulas no formato:
Nome da Aula|Descrição da Aula|Carga Horária
- eventos.txt: Armazena os dados dos eventos no formato:
Nome do Evento|Descrição do Evento|Data do Evento

## Estilo
O estilo da aplicação é definido no arquivo static/styles.css.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

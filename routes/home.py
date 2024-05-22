from flask import Blueprint, render_template

# Define o Blueprint para as rotas relacionadas à página inicial
home_route = Blueprint('home', __name__)

# Define o caminho dos arquivos onde as informações de aulas e eventos são armazenadas
DATA_FILE = 'database/evento.txt'
AULAS_FILE = 'database/aulas.txt'

# Função para carregar as aulas do arquivo
def carregar_aulas():
    aulas = []
    with open(AULAS_FILE, 'r') as file:
        aulas = [line.strip().split('|') for line in file.readlines()]
        # Cada linha do arquivo representa uma aula, separada por '|'
    return aulas

# Função para carregar os eventos do arquivo
def carregar_eventos():
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
        # Cada linha do arquivo representa um evento, separada por '|'
    return eventos

# Rota para a página inicial
@home_route.route('/')
def home():
    # Carrega as aulas e eventos do arquivo
    aulas = carregar_aulas()
    eventos = carregar_eventos()
    # Renderiza a página inicial com as informações carregadas
    return render_template('home/home.html', aulas=aulas, eventos=eventos)
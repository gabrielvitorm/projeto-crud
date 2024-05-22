from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

DATA_FILE = 'database/evento.txt'
AULAS_FILE = 'database/aulas.txt'

def carregar_aulas():
    aulas = []
    with open(AULAS_FILE, 'r') as file:
        aulas = [line.strip().split('|') for line in file.readlines()]
    return aulas

def carregar_eventos():
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
    return eventos

@home_route.route('/')
def home():
    aulas = carregar_aulas()
    eventos = carregar_eventos()
    return render_template('home/home.html', aulas=aulas, eventos=eventos)
from flask import Blueprint, render_template, request, url_for, redirect
import os

# Estou usando o Blueprint para separar as rotas das aulas e dos eventos
aula_route = Blueprint('aula', __name__)
AULAS_FILE = 'database/aulas.txt'

# Rota para a página inicial que lista as aulas
@aula_route.route('/')
def home_page():
    aulas = []
    # Abre o arquivo de aulas e lê as informações
    with open(AULAS_FILE, 'r') as file:
        aulas = [line.strip().split('|') for line in file.readlines()]
        # Cada linha do arquivo representa uma aula, separada por '|'
    return render_template('aula/home_aula.html', aulas=aulas)

# Rota para criar uma nova aula
@aula_route.route('/new', methods=['GET', 'POST'])
def nova_aula():
    if request.method == 'POST':
        # Recebe os dados do formulário e os adiciona ao arquivo de aulas
        aula = request.form['title'] + '|' + request.form['description'] + '|' + request.form['hours'] + '\n'
        with open(AULAS_FILE, 'a') as file:
            file.write(aula)
        return redirect(url_for('aula.home_page'))
    # Exibe o formulário para criar uma nova aula
    return render_template('aula/criar_aula.html')

# Rota para atualizar uma aula existente
@aula_route.route('/update/<int:line_number>', methods=['GET', 'POST'])
def update_aula(line_number):
    cursos = []
    with open(AULAS_FILE, 'r') as file:
        cursos = [line.strip().split('|') for line in file.readlines()]
    if request.method == 'POST':
        # Atualiza os dados da aula no arquivo
        cursos[line_number] = [request.form['title'], request.form['description'], request.form['hours']]
        with open(AULAS_FILE, 'w') as file:
            for curso in cursos:
                file.write('|'.join(curso) + '\n')
        return redirect(url_for('aula.home_page'))
    # Exibe o formulário de atualização da aula
    return render_template('aula/update_aula.html', curso=cursos[line_number], line_number=line_number)

# Rota para deletar uma aula existente
@aula_route.route('/delete/<int:line_number>', methods=['GET', 'POST'])
def delete_aula(line_number):
    cursos = []
    with open(AULAS_FILE, 'r') as file:
        cursos = [line.strip().split('|') for line in file.readlines()]
    # Remove a aula selecionada do arquivo
    cursos.pop(line_number)
    with open(AULAS_FILE, 'w') as file:
        for curso in cursos:
            file.write('|'.join(curso) + '\n')
    return redirect(url_for('aula.home_page'))
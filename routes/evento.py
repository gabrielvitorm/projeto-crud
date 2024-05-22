from flask import Blueprint, render_template, request, url_for, redirect

# Define o Blueprint para as rotas relacionadas aos eventos
evento_route = Blueprint('evento', __name__)

# Define o caminho do arquivo onde os eventos serão armazenados
DATA_FILE = 'database/evento.txt'

# Rota para a página inicial que lista os eventos
@evento_route.route('/')
def home_page_evento():
    eventos = []
    # Abre o arquivo de eventos e lê as informações
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
        # Cada linha do arquivo representa um evento, separada por '|'
    return render_template('evento/home_evento.html', eventos=eventos)

# Rota para criar um novo evento
@evento_route.route('/new', methods=['GET', 'POST'])
def novo_evento():
    if request.method == 'POST':
        # Recebe os dados do formulário e os adiciona ao arquivo de eventos
        evento = request.form['title'] + '|' + request.form['description'] + '|' + request.form['date'] + '\n'
        with open(DATA_FILE, 'a') as file:
            file.write(evento)
        return redirect(url_for('evento.home_page_evento'))
    # Exibe o formulário para criar um novo evento
    return render_template('evento/criar_evento.html')

# Rota para atualizar um evento existente
@evento_route.route('/update/<int:line_number>', methods=['GET', 'POST'])
def update_evento(line_number):
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
    if request.method == 'POST':
        # Atualiza os dados do evento no arquivo
        eventos[line_number] = [request.form['title'], request.form['description'], request.form['date']]
        with open(DATA_FILE, 'w') as file:
            for evento in eventos:
                file.write('|'.join(evento) + '\n')
        return redirect(url_for('evento.home_page_evento'))
    # Exibe o formulário de atualização do evento
    return render_template('evento/update_evento.html', evento=eventos[line_number], line_number=line_number)

# Rota para deletar um evento existente
@evento_route.route('/delete/<int:line_number>', methods=['GET', 'POST'])
def delete_evento(line_number):
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
    # Remove o evento selecionado do arquivo
    eventos.pop(line_number)
    with open(DATA_FILE, 'w') as file:
        for evento in eventos:
            file.write('|'.join(evento) + '\n')
    return redirect(url_for('evento.home_page_evento'))
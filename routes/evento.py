from flask import Blueprint, render_template, request, url_for, redirect

evento_route = Blueprint('evento', __name__)

DATA_FILE = 'database/evento.txt'

# 1 - Essa primeira rota serve para listar as aulas que estão no "banco de dados" em txt, é necessário abrir uma lista no começo da função, pois vai ser atribuido um dicionário a esse txt. Também é necessário declarar uma Variável para receber o arquivo txt que nesse caso é a variável "DATA_FILE"
@evento_route.route('/')
def home_page_evento():
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()] # Essa é uma usabilidade da biblioteca os para ler as informações da linha.
    return render_template('evento/home_evento.html', eventos=eventos) #É necessário atribuir a variável para usar no HTML com o Jinja

# 1 - Essa segunda rota serve para criar uma aula através de um formulário Html
@evento_route.route('/new', methods=['GET', 'POST'])
def novo_evento():
    if request.method == 'POST': #Metodo POST serve para receber os dados do formulário
        evento = request.form['title'] + '|' + request.form['description'] + '|' + request.form['date'] + '\n' #essas tags são definidas no formulário com o id e a variável aula vai receber essas informações
        with open(DATA_FILE, 'a') as file:
            file.write(evento)
        return redirect(url_for('evento.home_page_evento'))
    return render_template('evento/criar_evento.html')

@evento_route.route('/update/<int:line_number>', methods=['GET', 'POST'])
def update_evento(line_number):
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines]
    if request.method == 'POST':
        eventos[line_number] = [request.form['title'], request.form['description'], request.form['date']]
        with open (DATA_FILE, 'w') as file:
            for evento in eventos:
                file.write('|'.join(evento) + '\n')
        return redirect(url_for('evento.home_page_evento'))
    return render_template('evento/update_evento.html', evento=eventos[line_number], line_number=line_number)

@evento_route.route('/delete/<int:line_number>', methods=['GET', 'POST'])
def delete_evento(line_number):
    eventos = []
    with open(DATA_FILE, 'r') as file:
        eventos = [line.strip().split('|') for line in file.readlines()]
    eventos.pop(line_number)
    with open (DATA_FILE, 'w') as file:
            for evento in eventos:
                file.write('|'.join(evento) + '\n')
    return redirect(url_for('evento.home_page_evento'))

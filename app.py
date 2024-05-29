from flask import Flask
from routes.aula import aula_route
from routes.evento import evento_route
from routes.home import home_route
from routes.sobre import sobre_route

# Cria uma instância do Flask
app = Flask(__name__)

# Registra os blueprints das rotas
app.register_blueprint(home_route)  # Rota para a página inicial
app.register_blueprint(aula_route, url_prefix='/aula')  # Rota para as operações relacionadas às aulas
app.register_blueprint(evento_route, url_prefix='/evento')  # Rota para as operações relacionadas aos eventos
app.register_blueprint(sobre_route, url_prefix='/sobre') # Rota para as operações relacionadas a página sobre

# Inicia o servidor Flask em modo de depuração
app.run(debug=True)
from flask import Flask
from routes.aula import aula_route
from routes.evento import evento_route
from routes.home import home_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(aula_route, url_prefix='/aula')
app.register_blueprint(evento_route, url_prefix='/evento')

app.run(debug=True)
from flask import Blueprint, render_template

sobre_route = Blueprint('sobre', __name__)

@sobre_route.route('/')
def pag_sobre():
    return render_template('sobre/sobre.html')
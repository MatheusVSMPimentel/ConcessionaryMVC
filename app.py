from flask import Flask
from markupsafe import escape
from flask import render_template
from models.Veiculo import Veiculo

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return render_template('index.html', name= Veiculo())
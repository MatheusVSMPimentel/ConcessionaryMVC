from flask import Flask
from markupsafe import escape
from flask import render_template
from models.Veiculo import Veiculo
from flask_migrate import Migrate

from models.Veiculo import db
from routes.veiculos_bp import veiculos_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(veiculos_bp, url_prefix='/veiculos')


if __name__ == '__main__':
    app.debug = True
    app.run()
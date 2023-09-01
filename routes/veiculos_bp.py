#Esse Arquivo conecta o APP.PY com o Arquivo controllers/Veiculos.PY utilizando a biblioteca BluePrint

from flask import Blueprint

from controllers.VeiculosController import index, store, show, update, delete

#criando novo objeto BLUEPRINT e disponibilizando ele no import se você mudar o 1º parametro('veiculos_bp') aqui tera que mudar no APP.PY
veiculos_bp = Blueprint('veiculos_bp', __name__)

#Essa rota pde ser crua ou ter um prefixo adicionado no APP.PY
veiculos_bp.route('/', methods=['GET'])(index)
veiculos_bp.route('/create', methods=['POST'])(store)

veiculos_bp.route('/<int:user_id>', methods=['GET'])(show)
veiculos_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
veiculos_bp.route('/<int:user_id>', methods=['DELETE'])(delete)
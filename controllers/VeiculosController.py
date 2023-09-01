import sys
from flask import render_template, redirect, url_for, request, abort

from models.Veiculo import Veiculo, db

def index():
    return render_template('cadastro.html')

def store():
    addVeiculo = Veiculo(
    request.form.get("Tipo"),
    request.form.get("Cor"),
    request.form.get("Marca"),
    request.form.get("Model"),
    request.form.get("AnoFabricacao"),
    request.form.get("Novo"),
    request.form.get("KmRodados"),
    request.form.get("Leilao"),
    request.form.get("Parcela"))
    db.session.add(addVeiculo)
    
def show(userId):
    ...

def update(userId):
    ...

def delete(userId):
    ...
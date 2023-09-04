import sys
from flask import render_template, redirect, url_for, request, abort

from models.Veiculos import Veiculo, db
from sqlalchemy import select
from sqlalchemy.orm import Session

def index():
    with Session(db) as session:
    # query for ``User`` objects
        veiculos = db.session.query(Veiculo).all()

    return render_template('index.html', veiculos = veiculos)

def store():
    if(request.method == 'GET'):
        return render_template('cadastro.html')
    if(request.form.getlist):
        with Session(db) as session:
            session.begin()
        try:
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
        except:
            session.rollback()
            raise
        else:
            session.commit()

    return index()
def show(userId):
    ...

def update(userId):
    ...

def delete(userId):
    ...
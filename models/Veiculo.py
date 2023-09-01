from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiculo(db.Model):
    __tablename__ = 'Veiculo'
    Id = db.Column(db.Integer, primary_key=True)
    Tipo = db.Column(db.Integer)
    Cor = db.Column(db.String(70))
    Marca = db.Column(db.String(70))
    Modelo = db.Column(db.String(70))
    AnoFabricacao = db.Column(db.String(20))
    Novo = db.Column(db.Boolean)
    KmRodados = db.Column(db.Integer)
    Leilao = db.Column(db.Boolean)
    Parcela = db.Column(db.Boolean)
    
    def __init__(self, tipo:int, cor:str, marca:str, modelo:str, anoFabricacao:str, novo:bool, kmRodados:int, leilao:bool,parcela:bool ):
        self.Tipo = tipo
        self.Cor = cor
        self.Marca = marca
        self.Modelo = modelo
        self.AnoFabricacao = anoFabricacao
        self.Novo = novo
        self.KmRodados = kmRodados
        self.Leilao = leilao
        self.Parcela = parcela

    @property
    def serialize(self):
        return {
            'Id': self.Id,
            'Tipo': self.Tipo,
            'Cor': self.Cor,
            'Marca': self.Marca,
            'Modelo': self.Modelo,
            'AnoFabricacao': self.AnoFabricacao,
            'Novo': self.Novo,
            'KmRodados': self.KmRodados,
            'Leilao': self.Leilao,
            'Parcela': self.Parcela
        }
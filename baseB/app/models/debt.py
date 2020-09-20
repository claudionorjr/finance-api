from . import db
from app.models.encryptor import Encryptor

class Debt(db.Model):

    __tablename = "debts"
    id = db.Column(db.Integer, primary_key=True)
    estabelecimento = db.Column(Encryptor(100))
    valor = db.Column(db.Float)
    id_finance_personal = db.Column(db.Integer, db.ForeignKey("finance_personal.id"))

    def __repr__(self):
        pass

    def to_json(self):
        pass
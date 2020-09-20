from . import db
from app.models.encryptor import Encryptor

class FinancialAssets(db.Model):

    __tablename = "financial_assets"
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    valor = db.Column(db.Float)
    id_finance_personal = db.Column(db.Integer, db.ForeignKey("finance_personal.id"))
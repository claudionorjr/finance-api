from . import db
from app.models.encryptor import Encryptor

class FinancePersonal(db.Model):

    __tablename__ = 'finance_personal'
    id = db.Column(db.Integer, primary_key=True)
    idade = db.Column(Encryptor(100))
    endereco = db.Column(Encryptor(100))
    id_personal = db.Column(db.Integer, nullable=False)
    debts = db.relationship("Debt", backref="finance_personal")
    incomes = db.relationship("Income", backref="finance_personal",)
    financial_assets = db.relationship("FinancialAssets", backref="finance_personal")

    def __repr__(self):
        pass
        
    def to_json(self):
        pass


from . import db
from app.models.encryptor import Encryptor

class Personal(db.Model):

    __tablename__ = 'personal'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(Encryptor(100))
    rg = db.Column(Encryptor(100))
    nome_completo = db.Column(Encryptor(200))
    endereco = db.Column(Encryptor(200))
    data_nascimento = db.Column(Encryptor(100))
    incomes = db.relationship("Income", backref="personal",)

    def __repr__(self):
        return f'<Personal id={self.id}\
            cpf={self.cpf} rg={self.rg} nome_completo={self.nome_completo}\
            endereço={self.endereco} data_nascimento={self.data_nascimento}'
        
    def to_json(self):
        json_generate = {
            'cpf': self.cpf,
            'rg': self.rg,
            'nome_completo': self.nome_completo,
            'endereco': self.endereco,
            'data_nascimento': self.data_nascimento
        }
        return json_generate


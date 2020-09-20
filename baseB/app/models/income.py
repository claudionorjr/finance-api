from . import db


class Income(db.Model):

    __tablename = 'incomes'
    id = db.Column(db.Integer, primary_key=True)
    tipo= db.Column(db.String(50))
    valor = db.Column(db.Float)
    id_finance_personal = db.Column(db.Integer, db.ForeignKey("finance_personal.id"))

    def __repr__(self):
        return f'<Income id={self.id}, tipo={self.tipo}, valor={self.valor}'

    def to_json(self):
        json_generate = {
            'tipo': self.tipo,
            'valor': self.valor
        }
        return json_generate
   
        
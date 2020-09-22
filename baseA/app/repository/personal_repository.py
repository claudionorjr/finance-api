from app.models.personal import Personal
from app.models.income import Income
from app.models import db
from sqlalchemy.exc import SQLAlchemyError

class PersonalRepository:

    def get_by_cpf(self, cpf):
        query = Personal.query.filter_by(cpf=cpf).first()
        return query

    def save(self, personal):
        try:
            query = Personal(
                cpf=personal['cpf'],
                rg=personal['rg'],
                nome_completo=personal['nome_completo'],
                endereco=personal['endereco'],
                data_nascimento=personal['data_nascimento']
            )
            db.session.add(query)
            db.session.commit()

            rendas = []
            for renda in personal['lista_rendas']:
                print(renda)
                income = Income(tipo=renda['tipo'], valor=renda['valor'])
                income.personal = query
                print(income)
                rendas.append(income)
            
            db.session.add_all(rendas)
            db.session.commit()

            db.session.refresh(query)
            return query.id
        except SQLAlchemyError:
            print("Erro ao salvar")

from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Personal, Income
from .errors import no_content


@api.route('/personal/<string:cpf>')
def get_user(cpf):
    personal = Personal.query.filter_by(cpf=cpf).first()
    if personal != None:

        income = Income.query.filter_by(personal=personal).all()

        json_return = {
            'dadosPessoais': personal.to_json(),
            'rendas':[income_json.to_json() for income_json in income]
        }

        return jsonify(json_return)
    
    return no_content("Nenhum dado encontrado")

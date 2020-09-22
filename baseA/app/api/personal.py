from flask import jsonify, request, current_app, url_for
from . import api
from .errors import no_content, bad_request, not_allowed_method
from app.services.personal_service import PersonalService
from app.services.income_service import IncomeService

@api.route('/personal/<string:cpf>')
def get_personal(cpf):

    personal = PersonalService().get_by_cpf(cpf)

    if personal != None:

        income = IncomeService().get_all_by_personal(personal)

        json_return = {
            'dadosPessoais': personal.to_json(),
            'rendas':[income_json.to_json() for income_json in income]
        }

        return jsonify(json_return)
    
    return no_content("Nenhum dado encontrado")


@api.route('/register', methods=['POST'])
def register_personal():
    print("Register")
    if(request.method == 'POST'):
        msg, status = PersonalService().register_personal(request.json)
        if status == 200:
            return msg_success_register(msg)
        
        return bad_request(msg)


def msg_success_register(msg):
    return jsonify({'message': msg})
from app.repository.personal_repository import PersonalRepository
from app.services.finance_personal_service import FinancePersonalService
from app.exceptions import ValidationError

class PersonalService:
    
    def get_by_cpf(self, cpf):
        query = PersonalRepository().get_by_cpf(cpf)
        return query

    """
    TODO: Validar retorno do serviço FinancePersonal, 
    pois os dados não devem ser commitado caso ocorra algum erro
    na resposta do servidor
    """
    def register_personal(self, request_json):
        if self._validate_keys(request_json):
            personal = {
                'cpf' : request_json['cpf'],
                'rg' : request_json['rg'],
                'nome_completo' : request_json['nomeCompleto'],
                'endereco' : request_json['endereco'],
                'data_nascimento' : request_json['dataNascimento'],
                'lista_rendas' : request_json['listaRendas']
            }
            
            id_personal = PersonalRepository().save(personal)

            print(id_personal, "ID DA PESSOA")

            finance_personal = {
                'idade' : 25, 
                'lista_dividas' : request_json['listaDividas'],
                'lista_ativos' : request_json['listaAtivos'],
                'endereco' : request_json['endereco'],
                'id_personal' : id_personal
            }

            response = FinancePersonalService().send(finance_personal)
            print(response)
            return ("cadastro realizado com sucesso", 200)
        else:
            return ("chaves inválidas no json", 401)


    # TODO: melhorar validação, pois é preciso passar duas vazes pelas chaves. 1 na validação e outra no commit
    def _validate_keys(self, request_json):
        try:
            request_json['cpf'],
            request_json['rg'],
            request_json['nomeCompleto'],
            request_json['endereco'],
            request_json['dataNascimento'],
            request_json['listaRendas']
            for renda in request_json['listaRendas']:
                renda['tipo']
                renda['valor']
            for ativo in request_json['listaAtivos']:
                ativo['tipo']
                ativo['valor']
            for divida in request_json['listaDividas']:
                divida['estabelecimento']
                divida['data_divida']
                divida['valor']

            return True
        except KeyError:
            return False

    def send_api_finance_personal(finance_personal):
        pass
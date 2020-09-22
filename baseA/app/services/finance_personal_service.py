import requests

"""
TODO: Classe precissa refatorada para obter a conexão do eureka server
     e os dados de login da variavel de ambiente
"""
class FinancePersonalService:
    """Classe responsável por fazer as requisições para a base b"""
    def __init__(self):
        self.login = "lucas@lucas.com"
        self.passwod = "cat"
        self.url = "http://localhost:3001/api/v1/register/financePersonal"

    def send(self, finance_personal):
        response = self._post(finance_personal)
        return response


    def _post(self, payload):
        r = requests.post(self.url, json=payload, auth=(self.login, self.passwod))
        return r
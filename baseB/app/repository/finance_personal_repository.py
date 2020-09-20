from app import db
from app.models import FinancePersonal, Debt, FinancialAssets, Income

class FinancePersonalRepository:

    def get_financePersonal_by_id(self, id: int) => dict:
        finance_personal = FinancePersonal.query.filter_by(id=id).first()
        debts = Debt.query.filter_by(finance_personal=finance_personal).all()
        financial_assets = FinancialAssets.query.filter_by(finance_personal=finance_personal).all()
        incomes = Income.query.filter_by(finance_personal=finance_personal).all()

        data_dict = {
            'dados_financeiros': {
                'idade': finance_personal.idade,
                'endereco': finance_personal.endereco,
                'dividas':[debt_json.to_json() for debts_json in debts]
                'ativosFinanceiros': [assets_json.to_json() for assets_json in financial_assets]
                'rendas': [income_json.to_json() for income_json in incomes]
            }
        }
        return data_dict
    
    def get_all_financePersonal(self) => list:
        all_finances = []
        finance_personal = FinancePersonal.query.all()
        for personal in finance_personal:
            debts = Debt.query.filter_by(finance_personal=personal).all()
            financial_assets = FinancialAssets.query.filter_by(finance_personal=personal).all()
            incomes = Income.query.filter_by(finance_personal=personal).all()

            data_dict = {
                'dados_financeiros': {
                    'idade': finance_personal.idade,
                    'endereco': finance_personal.endereco,
                    'dividas':[debt_json.to_json() for debts_json in debts]
                    'ativosFinanceiros': [assets_json.to_json() for assets_json in financial_assets]
                    'rendas': [income_json.to_json() for income_json in incomes]
                }
            }

            all_finances.append(data_dict)
        

        return all_finances

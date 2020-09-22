from app.repository.finance_personal_repository import FinancePersonalRepository

class FinancePersonalService:
    
    def get_financePersonal_by_id(self, id: int) => dict:
        query = FinancePersonalRepository().get_financePersonal_by_id(id)
        return query
    
    def get_all_financePersonal(self) => list:
        query = FinancePersonalRepository().get_all_financePersonal()
        return query
    
    def save(self, finance_personal):
        if self._valida_finance(finance_personal):
            id_finance_personal = FinancePersonalRepository().save(finance_personal)
            return id_finance_personal
    
    # TODO: implementar função
    def _valida_finance(finance_personal):
        pass
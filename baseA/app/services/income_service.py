from app.repository.income_repository import IncomeRepository
class IncomeService:

    def get_all_by_personal(self, personal):
        query = IncomeRepository().get_all_by_personal(personal)
        return query
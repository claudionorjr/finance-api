from app.models import db
from app.models.income import Income

class IncomeRepository:
    
    def get_all_by_personal(self, personal):
        query = Income.query.filter_by(personal=personal).all()
        return query

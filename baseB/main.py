import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app
from app.models import Debt, FinancePersonal, Income, User, FinancialAssets, db

app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.app_context().push()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, FinancePersonal=FinancePersonal, 
                Income=Income, User=User, FinancialAssets=FinancialAssets,
                Debt=Debt)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3001)
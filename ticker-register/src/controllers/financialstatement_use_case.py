from ..models.use_case_processor import UseCaseProcessor
from ..models.db_interface import DbInterface
from ..models.financialstatement import FinancialStatement
from typing import Dict
import datetime as dt

class FinancialStatementUseCase(UseCaseProcessor):
    def process(self, db: DbInterface, message: Dict):
        new_fstatement = FinancialStatement(
            message['ticker_code'],
            dt.datetime.strptime(message['statement_date'], '%Y-%m-%d').date(),
            message['stocks_amount'],
            message['div_yield'],
            message['assets'],
            message['disponibility'],
            message['current_assets'],
            message['gross_debt'],
            message['net_debt'],
            message['liquid_equity'],
            message['net_revenue'],
            message['ebit'],
            message['liquid_profit']
        )
        db.insert_statement(new_fstatement)
        
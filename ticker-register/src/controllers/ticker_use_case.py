from ..models.use_case_processor import UseCaseProcessor
from ..controllers.db_accessor import DbAccessor
from ..models.ticker import Ticker
from typing import Dict

class TickerUseCase(UseCaseProcessor):
    
    def process(self, db: DbAccessor, message: Dict):
        new_ticker = Ticker(
        message['ticker_code'],
        message['enterprise_name'],
        message['sector_id']
        )      
        db.insert_ticker(new_ticker)
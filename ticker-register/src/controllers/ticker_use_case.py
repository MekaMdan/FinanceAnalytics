from ..models.use_case_processor import UseCaseProcessor
from ..models.db_interface import DbInterface
from ..models.ticker import Ticker
from typing import Dict

class TickerUseCase(UseCaseProcessor):
    def process(self, db: DbInterface, message: Dict):
        new_ticker = Ticker(
        message['ticker_code'],
        message['enterprise_name'],
        message['sector_id']
        )      
        db.insert_ticker(new_ticker)
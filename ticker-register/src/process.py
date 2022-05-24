from .controllers.db_accessor import DbAccessor
from typing import Dict
from .models.ticker import Ticker

def process(message: Dict):
    db = DbAccessor.get_impl('postgresql')
    new_ticker = Ticker(
        message['ticker_code'],
        message['enterprise_name'],
        message['sector_id']
    )
    db.insert_ticker(new_ticker)
from ..models.use_case_processor import UseCaseProcessor
from ..models.db_interface import DbInterface
from ..models.price import Price
from typing import Dict
import datetime as dt

class PriceUseCase(UseCaseProcessor):
    def process(self, db: DbInterface, message: Dict):
        new_price = Price(
            message['ticker_code'],
            message['price_value'],
            dt.datetime.strptime(message['price_date'], '%Y-%m-%d').date()
        )

        db.insert_price(new_price)

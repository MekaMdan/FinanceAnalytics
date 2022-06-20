import datetime as dt
from typing import Dict

class Price:
    ticker_code: str
    price_value: float
    price_date: dt.date

    def __repr__(self) -> str:
        return f'''
        Price(
            ticker_code: {self.ticker_code},
            price_value: {self.price_value},
            price_date: {self.price_date}
        )
        '''

    def serialize(self) -> Dict:
        return {
            'ticker_code': self.ticker_code,
            'price_value': self.price_value,
            'price_date': self.price_date.strftime('%Y-%m-%d')
        }

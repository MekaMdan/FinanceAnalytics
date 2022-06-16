import datetime as dt
from typing import Dict

class Price:
    ticker_code: str
    price: float
    price_date: dt.date

    def __repr__(self) -> str:
        return f'''
        Price(
            ticker_code: {self.ticker_code},
            price: {self.price},
            price_date: {self.price_date}
        )
        '''

    def seriarize(self) -> Dict:
        return {
            'ticker_code': self.ticker_code,
            'price': self.price,
            'price_date': self.price_date.strftime('%Y-%m-%d')
        }

import datetime as dt

class Price:
    ticker_code: str
    price: float
    price_date: dt.date

    def __init__(self, ticker_code: str, price: float, price_date: dt.date):
        self.ticker_code = ticker_code
        self.price = price
        self.price_date = price_date

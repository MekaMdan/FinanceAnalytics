import datetime as dt

class Price:
    ticker_id: int
    price: float
    price_date: dt.date

    def __init__(self, ticker_id: int, price: float, price_date: dt.date):
        self.ticker_id = ticker_id
        self.price = price
        self.price_date = price_date

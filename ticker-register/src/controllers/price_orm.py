from .base_orm import Base
from sqlalchemy import Column, Float, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .ticker_orm import TickerOrm
from ..models.price import Price

class PriceOrm(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    price_value = Column(Float)
    price_date = Column(Date)
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    ticker = relationship(TickerOrm)

    def __init__(self, price:Price, ticker_id: int):
        self.price_date = price.price_date
        self.price_value = price.price_value
        self.ticker_id = ticker_id
    
    def __repr__(self) -> str:
        return f'''
        Price(
            id: {self.id}
            ticker_code: {self.ticker.ticker_code},
            price_value: {self.price_value},
            price_date: {self.price_date}
        )
        '''
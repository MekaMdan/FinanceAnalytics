from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..models.ticker import Ticker
from ..controllers.sector_orm import SectorOrm
from .base_orm import Base

class TickerOrm(Base):
    __tablename__ = 'tickers'
    id = Column(Integer, primary_key=True)
    ticker_code = Column(String(5))
    enterprise_name = Column(String(32))
    sector_id = Column(Integer, ForeignKey('sectors.id'))
    sector = relationship(SectorOrm)

    def __init__(self,ticker:Ticker):
        self.ticker_code = ticker.ticker_code
        self.enterprise_name = ticker.enterprise_name
        self.sector_id = ticker.sector_id

    def __repr__(self) -> str:
        return f"Ticker({self.id}, {self.ticker_code}, {self.enterprise_name},\
{self.sector.sector_name})"

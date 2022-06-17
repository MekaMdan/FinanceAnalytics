from .base_orm import Base
from .ticker_orm import TickerOrm
from ..models.financialstatement import FinancialStatement
from sqlalchemy import BigInteger, Column, Integer, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship

class FinancialStatementOrm(Base):
    __tablename__ = 'financialstatements'
    id = Column(Integer, primary_key=True)
    ticker_id = Column(Integer, ForeignKey('tickers.id'))
    ticker = relationship(TickerOrm)
    statement_date = Column(Date)
    stocks_amount = Column(BigInteger)
    div_yield = Column(Numeric)
    assets = Column(BigInteger)
    disponibility = Column(BigInteger)
    current_assets = Column(BigInteger)
    gross_debt = Column(BigInteger)
    net_debt = Column(BigInteger)
    liquid_equity = Column(BigInteger)
    net_revenue = Column(BigInteger)
    ebit = Column(BigInteger)
    liquid_profit = Column(BigInteger)

    def __init__(self, f_statement: FinancialStatement, ticker_id: int):
        self.statement_date = f_statement.statement_date
        self.stocks_amount = f_statement.stocks_amount
        self.div_yield = f_statement.div_yield
        self.assets = f_statement.assets
        self.disponibility = f_statement.disponibility
        self.current_assets = f_statement.current_assets
        self.gross_debt = f_statement.gross_debt
        self.net_debt = f_statement.net_debt
        self.liquid_equity = f_statement.liquid_equity
        self.net_revenue = f_statement.net_revenue
        self.ebit = f_statement.ebit
        self.liquid_profit = f_statement.liquid_profit
        self.ticker_id = ticker_id

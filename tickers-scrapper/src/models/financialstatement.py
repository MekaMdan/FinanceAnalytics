import datetime as dt
from typing import Dict

class FinancialStatement:
    ticker_code: str
    statement_date: dt.date
    stocks_amount: int
    div_yield: float
    assets: int
    disponibility: int
    current_assets: int
    gross_debt: int
    net_debt: int
    liquid_equity: int
    net_revenue: int
    ebit: int
    liquid_profit: int

    def __repr__(self) -> str:
        return f'''
        FinancialStatement(
            ticker_code: {self.ticker_code},
            statement_date: {self.statement_date},
            stocks_amount: {self.stocks_amount},
            div_yield: {self.div_yield},
            assets: {self.assets},
            disponibility: {self.disponibility},
            current_assets: {self.current_assets},
            gross_debt: {self.gross_debt},
            net_debt: {self.net_debt},
            liquid_equity: {self.liquid_equity},
            net_revenue: {self.net_revenue},
            ebit: {self.ebit},
            liquid_profit: {self.liquid_profit}
        )
        '''
    
    def serialize(self) -> Dict:
        return {
            'ticker_code': self.ticker_code,
            'statement_date': self.statement_date.strftime('%Y-%m-%d'),
            'stocks_amount': self.stocks_amount,
            'div_yield': self.div_yield,
            'assets': self.assets,
            'disponibility': self.disponibility,
            'current_assets': self.current_assets,
            'gross_debt': self.gross_debt,
            'net_debt': self.net_debt,
            'liquid_equity': self.liquid_equity,
            'net_revenue': self.net_revenue,
            'ebit': self.ebit,
            'liquid_profit': self.liquid_profit
        }

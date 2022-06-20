from typing import Dict


class Ticker:
    '''
    Ticker is a data object that represents a Brazilian Enterprise from B3 entry
    - ticker_code: A code that represents a stock in B3 (eg. CAML3)
    - enterprise_name: the enterprise_name that represents that stock
    - sector_id: the id from the stock's economic sector
    '''
    ticker_code: str
    enterprise_name: str
    sector_id: int

    def __init__(self, ticker_code: str, enterprise_name: str, sector_id: int):
        self.ticker_code = ticker_code
        self.enterprise_name = enterprise_name
        self.sector_id = sector_id

    def __repr__(self) -> str:
        return f"Ticker({self.ticker_code}, {self.enterprise_name},\
{self.sector_id})"

    def serialize(self) -> Dict:
        return {
            'ticker_code':self.ticker_code, 
            'enterprise_name':self.enterprise_name,
            'sector_id':self.sector_id
        }

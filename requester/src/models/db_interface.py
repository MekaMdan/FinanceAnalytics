from ..controllers.ticker_orm import TickerOrm
from typing import List

class DbInterface:
    '''
    This abstract class specifies the expected methods that a db driver has to
    implement.
    '''
    def get_tickers(self) -> List[TickerOrm]:
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def connect_to_db(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
        
    def disconnect_db(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
    
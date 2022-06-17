from .ticker import Ticker
from .price import Price
from .financialstatement import FinancialStatement

class DbInterface:
    '''
    This abstract class specifies the expected methods that a db driver has to
    implement.
    '''
    def insert_ticker(self, ticker: Ticker):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def insert_price(self, price: Price):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def insert_statement(self, f_statement: FinancialStatement):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def connect_to_db(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
        
    def disconnect_db(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
    
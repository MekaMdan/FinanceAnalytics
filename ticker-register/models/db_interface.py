from ticker import Ticker


class DbInterface:
    '''
    This abstract class specifies the expected methods that a db driver has to
    implement.
    '''
    def insert_ticker(self, ticker: Ticker):
        raise NotImplementedError("This method has not been defined yet")


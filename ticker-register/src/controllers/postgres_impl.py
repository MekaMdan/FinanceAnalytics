from ..models.db_interface import DbInterface
from ..models.ticker import Ticker
from psycopg2 import connect, DatabaseError
from psycopg2.extensions import connection, cursor
from ..config import config 

class PostgresImpl(DbInterface):
    '''
    This controller is a Postgres' db_interface implementation
    '''
    db_connection: connection
    db_cursor: cursor
    
    def __init__(self):
        self.db_connection = None
        self.db_cursor = None
        
    def insert_ticker(self, ticker: Ticker):
        pass

    def connect_to_db(self):
        try:
            # read connection parameters
            params = config(section='postgresql')

            # Connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database... ')
            self.db_connection = connect(**params)

            # create a cursor
            self.db_cursor = self.db_connection.cursor()
        except (Exception, DatabaseError) as error:
            print(error)

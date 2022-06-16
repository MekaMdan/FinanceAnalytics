from ..models.db_interface import DbInterface
from ..models.ticker import Ticker
from ..config import config 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..controllers.ticker_orm import TickerOrm
from typing import List

class PostgresImpl(DbInterface):
    '''
    This controller is a Postgres' db_interface implementation
    '''
    db_session: Session
    
    def __init__(self):
        self.db_session = None
        
    def get_tickers(self) -> List[TickerOrm]:
        exists_in_db = self.db_session.query(TickerOrm).all()
        return exists_in_db

    def connect_to_db(self):
        try:
            # read connection parameters
            params = config(section='postgresql')
            user = params["user"]
            password = params["password"]
            host=params["host"]
            database=params["database"]
            port=params["port"]
            # Connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database... ')
            connection_string = \
                f"postgresql://{user}:{password}@{host}:{port}/{database}"
            engine = create_engine(connection_string)
            self.db_session = sessionmaker(engine)()
        except (Exception) as error:
            print(error)

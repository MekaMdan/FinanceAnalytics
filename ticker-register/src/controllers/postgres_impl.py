from ..models.db_interface import DbInterface
from ..models.ticker import Ticker
from ..config import config 
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..controllers.ticker_orm import TickerOrm
from ..models.price import Price
from ..controllers.price_orm import PriceOrm
from ..models.financialstatement import FinancialStatement
from ..controllers.financialstatement_orm import FinancialStatementOrm

class PostgresImpl(DbInterface):
    '''
    This controller is a Postgres' db_interface implementation
    '''
    db_session: Session
    
    def __init__(self):
        self.db_session = None
        
    def insert_ticker(self, ticker: Ticker) -> TickerOrm:
        try:
            exists_in_db = self.db_session.query(TickerOrm).filter_by(
                ticker_code = ticker.ticker_code).first() is not None
            if (not exists_in_db):
                new_ticker = TickerOrm(ticker)
                self.db_session.add(new_ticker)
                self.db_session.commit()
                return new_ticker
            else:
                print(f'[INFO] Ticker with code {ticker.ticker_code} already exists')
        except Exception as error:
            print(error)
            self.db_session.rollback()

    def insert_price(self, price:Price) -> PriceOrm:
        try:
            ticker= self.db_session.query(TickerOrm).filter_by(
                ticker_code = price.ticker_code).first()
            if(ticker is None):
                raise Exception("Inexistent ticker")
            exists_in_db = self.db_session.query(PriceOrm).filter(
                and_(
                    PriceOrm.ticker_id==ticker.id, 
                    PriceOrm.price_date==price.price_date)
            ).first() is not None
            if (not exists_in_db):
                new_price = PriceOrm(price, ticker.id)
                self.db_session.add(new_price)
                self.db_session.commit()
                return new_price
            else:
                print(f'[INFO] data already exists')
        except Exception as error:
            print(error)
            self.db_session.rollback()

    def insert_statement(self, f_statement: FinancialStatement) -> FinancialStatementOrm:
        try:
            ticker = self.db_session.query(TickerOrm).filter_by(
                ticker_code = f_statement.ticker_code).first()
            if(ticker is None):
                raise Exception("Inexistent ticker")
            exists_in_db = self.db_session.query(FinancialStatementOrm).filter(
                and_(
                    FinancialStatementOrm.ticker_id==ticker.id, 
                    FinancialStatementOrm.statement_date==f_statement.statement_date)
            ).first() is not None
            if (not exists_in_db):
                new_fstatement = FinancialStatementOrm(f_statement, ticker.id)
                self.db_session.add(new_fstatement)
                self.db_session.commit()
                return new_fstatement
            else:
                print(f'[INFO] data already exists')
        except Exception as error:
            print(error)
            self.db_session.rollback()
            
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

from unittest import TestCase, main
from ..controllers.postgres_impl import PostgresImpl
from ..models.ticker import Ticker
from ..controllers.ticker_orm import TickerOrm
from ..controllers.price_orm import PriceOrm
from ..models.price import Price
from ..models.financialstatement import FinancialStatement
from ..controllers.financialstatement_orm import FinancialStatementOrm
import datetime as dt

class TestPostgresImplementationMethods(TestCase):
    def test_connect_to_db(self):
        '''
        In order to this test succeed, an postgres instance must be up
        '''
        db = PostgresImpl()
        db.connect_to_db()
        self.assertIsNotNone(db.db_session)


    def test_insert_ticker(self):
        print("Testing insert_ticker")
        test_ticker = Ticker('CAML3','CAMIL',3)
        db = PostgresImpl()
        db.connect_to_db()
        try:
            ticker: TickerOrm = db.insert_ticker(test_ticker)
            added_ticker = db.db_session.query(TickerOrm).get(ticker.id)
            self.assertIsNotNone(
                added_ticker,
                'query results is None'
            )
        
            print(added_ticker)
            db.db_session.delete(added_ticker)
            db.db_session.commit()

        except Exception as error:
            print(error)
            db.db_session.rollback()
            
    def test_insert_price(self):
        print("Testing insert_price")
        test_ticker = Ticker('CAML3','CAMIL',3)
        db = PostgresImpl()
        db.connect_to_db()
        try:
            ticker: TickerOrm = db.insert_ticker(test_ticker)
            added_ticker = db.db_session.query(TickerOrm).get(ticker.id)
            
            test_price = Price('CAML3',9.9, dt.date(2022,6,15))
            price: PriceOrm = db.insert_price(test_price)
            added_price = db.db_session.query(PriceOrm).get(price.id)
            
            price_equal = db.insert_price(test_price)
            self.assertIsNotNone(
                added_price,
                'query_results is None'
            )
        
            print(added_price)
            db.db_session.delete(added_price)
            db.db_session.delete(added_ticker)
            db.db_session.commit()
    
        except Exception as error:
            print(error)
            db.db_session.rollback() 

    def test_insert_statement(self):
        print("Testing insert_statement")
        test_ticker = Ticker('CAML3','CAMIL',3)
        db = PostgresImpl()
        db.connect_to_db()
        try:
            ticker: TickerOrm = db.insert_ticker(test_ticker)
            added_ticker = db.db_session.query(TickerOrm).get(ticker.id)

            test_statement = FinancialStatement(
                'CAML3', dt.date(2022,2,28),360000000,
                3.8,7930970000,1630060000,4829110000,3430010000,
                1799950000, 9015860000, 2878800000, 527431000,
                477784000
            )
            statement = db.insert_statement(
                test_statement)
            added_fstatement = db.db_session.query(FinancialStatementOrm).get(
                statement.id)

            self.assertIsNotNone(
                added_fstatement,
                'query results is None'
            )

            print(added_fstatement)
            db.db_session.delete(added_fstatement)
            db.db_session.delete(added_ticker)
            db.db_session.commit()

        except Exception as error:
            print(error)
            db.db_session.rollback() 

if __name__ == '__main__':
    main()

from unittest import TestCase, main
from ..controllers.postgres_impl import PostgresImpl
from ..models.ticker import Ticker
from ..controllers.ticker_orm import TickerOrm
from ..controllers.price_orm import PriceOrm
from ..models.price import Price
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
                'query_results is None'
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

if __name__ == '__main__':
    main()

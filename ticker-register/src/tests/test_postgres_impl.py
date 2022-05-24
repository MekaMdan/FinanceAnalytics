from typing import List
from unittest import TestCase, main
from ..controllers.postgres_impl import PostgresImpl
from ..models.ticker import Ticker
from ..controllers.ticker_orm import TickerOrm
from sqlalchemy.orm import Session

class TestPostgresImplementationMethods(TestCase):
    def test_connect_to_db(self):
        '''
        In order to this test succeed, an postgres instance must be up
        '''
        db = PostgresImpl()
        db.connect_to_db()
        self.assertIsNotNone(db.db_session)

    def test_insert_ticker(self):
        test_ticker = Ticker('CAML3','CAMIL',3)
        db = PostgresImpl()
        db.connect_to_db()
        ticker: TickerOrm = db.insert_ticker(test_ticker)
        added_ticker = db.db_session.query(TickerOrm).get(ticker.id)
        self.assertIsNotNone(
            added_ticker,
            'query_results is None'
        )
    
        print(added_ticker)
        db.db_session.delete(added_ticker)
            
            

if __name__ == '__main__':
    main()

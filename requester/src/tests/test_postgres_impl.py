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

    def test_get_tickers(self):
        db = PostgresImpl()
        db.connect_to_db()
        
        tickers_in_db = db.get_tickers()
        self.assertIsNotNone(
            tickers_in_db,
            'query_results is None'
        )

        self.assertNotEqual(
            len(tickers_in_db), 0,
            'query result is empty'
        )

        print (f'{len(tickers_in_db)} tickers queried')
         

if __name__ == '__main__':
    main()

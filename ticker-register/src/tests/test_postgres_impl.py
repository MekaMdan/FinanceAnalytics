from unittest import TestCase, main
from ..controllers.postgres_impl import PostgresImpl
from ..models.ticker import Ticker

class TestPostgresImplementationMethods(TestCase):
    def test_connect_to_db(self):
        '''
        In order to this test succeed, an postgres instance must be up
        '''
        db = PostgresImpl()
        db.connect_to_db()
        self.assertIsNotNone(db.db_cursor)
        db.db_cursor.execute("SELECT version()")
        version = db.db_cursor.fetchone()
        print(version)

    def test_insert_ticker(self):
        test_ticker = Ticker('CAML3','CAMIL',3)
        db = PostgresImpl()
        db.insert_ticker(test_ticker)


if __name__ == '__main__':
    main()

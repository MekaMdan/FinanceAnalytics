from ..models.db_interface import DbInterface
from .postgres_impl import PostgresImpl
from ..models.accessor_interface import AccessorInterface

class DbAccessor(AccessorInterface):
    db_instance: DbInterface = None

    @staticmethod
    def get_impl(choosen_db:str) -> DbInterface:
        available_dbs = {
            'postgresql':PostgresImpl
        }
        if(not DbAccessor.db_instance):
            DbAccessor.db_instance = available_dbs[choosen_db]()
            DbAccessor.db_instance.connect_to_db()
        return DbAccessor.db_instance

    

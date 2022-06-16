from .controllers.db_accessor import DbAccessor
from .controllers.use_case_acessor import UseCaseAcessor
from typing import Dict

def process(message: Dict, routing_key: str):
    db = DbAccessor.get_impl('postgresql')
    usecase = UseCaseAcessor.get_impl(routing_key)()
    usecase.process(db, message)
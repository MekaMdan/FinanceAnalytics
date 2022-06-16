from typing import Dict
from .controllers.use_case_accessor import UseCaseAcessor

def process(message: Dict):
    service_source = message["source"]

    usecase = UseCaseAcessor.get_impl(service_source)()
    usecase.process()
from typing import Dict
from .controllers.use_case_acessor import UseCaseAcessor

def process(message: Dict):
    scrapping_source = message["source"]
    
    usecase = UseCaseAcessor.get_impl(scrapping_source)()
    usecase.process(message)

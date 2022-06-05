from ..models.scrapper_interface import ScrapperInterface
from .infomoney_scrapper import InfomoneyScrapper
from ..models.accessor_interface import AccessorInterface

class ScrapperAcessor(AccessorInterface):
    scrapper_instance: ScrapperInterface = None

    @staticmethod
    def get_impl(choosen_scapper:str) -> ScrapperInterface:
        available_scrappers = {
            'infomoney': InfomoneyScrapper
        }
        if(not ScrapperAcessor.scrapper_instance):
            ScrapperAcessor.scrapper_instance = available_scrappers[choosen_scapper]
        return ScrapperAcessor.scrapper_instance
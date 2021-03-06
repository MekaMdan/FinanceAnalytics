from ..models.accessor_interface import AccessorInterface
from ..models.use_case_processor import UseCaseProcessor
from ..controllers.infomoney_use_case import InfomoneyUseCase
from ..controllers.fundamentus_use_case import FundamentusUseCase

class UseCaseAcessor(AccessorInterface):
    use_case_instance: UseCaseProcessor = None

    @staticmethod
    def get_impl(choosen_instance: str) -> UseCaseProcessor:
        available_use_cases = {
            "infomoney": InfomoneyUseCase,
            "fundamentus": FundamentusUseCase
        }
        UseCaseAcessor.use_case_instance = available_use_cases[choosen_instance]
        return UseCaseAcessor.use_case_instance

        
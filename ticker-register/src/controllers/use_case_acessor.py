from ..models.accessor_interface import AccessorInterface
from ..models.use_case_processor import UseCaseProcessor
from ..controllers.ticker_use_case import TickerUseCase

class UseCaseAcessor(AccessorInterface):
    use_case_instance: UseCaseProcessor = None

    @staticmethod
    def get_impl(choosen_use_case: str) -> UseCaseProcessor:
        available_use_cases = {
            "ticker":TickerUseCase
        }

        if (not UseCaseAcessor.use_case_instance):
            UseCaseAcessor.use_case_instance = available_use_cases[choosen_use_case]
        return UseCaseAcessor.use_case_instance
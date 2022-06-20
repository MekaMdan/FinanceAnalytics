from ..models.accessor_interface import AccessorInterface
from ..models.use_case_processor import UseCaseProcessor
from ..controllers.ticker_use_case import TickerUseCase
from ..controllers.financialstatement_use_case import FinancialStatementUseCase
from ..controllers.price_use_case import PriceUseCase

class UseCaseAcessor(AccessorInterface):
    use_case_instance: UseCaseProcessor = None

    @staticmethod
    def get_impl(choosen_use_case: str) -> UseCaseProcessor:
        available_use_cases = {
            "ticker":TickerUseCase,
            "statement":FinancialStatementUseCase,
            "price":PriceUseCase
        }

        UseCaseAcessor.use_case_instance = available_use_cases[choosen_use_case]
        return UseCaseAcessor.use_case_instance
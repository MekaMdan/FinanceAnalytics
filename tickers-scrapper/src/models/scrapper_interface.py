from typing import Dict, List, Tuple
from .financialstatement import FinancialStatement
from .price import Price
from .ticker import Ticker

class ScrapperInterface:
    def scrap(self) -> List[Ticker]:
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def scrap(self, message:Dict) -> Tuple[Price, FinancialStatement]:
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
from typing import List
from .ticker import Ticker

class ScrapperInterface:
    def scrap(self) -> List[Ticker]:
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
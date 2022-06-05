from typing import List
from unittest import TestCase, main
from ..models.ticker import Ticker
from ..controllers.infomoney_scrapper import InfomoneyScrapper

class TestInfomoneyScrapper(TestCase):
    def test_scrapper(self):
        scrapper = InfomoneyScrapper()
        tickers = scrapper.scrap()
        
        self.assertIsNotNone(
            tickers,
            "tickers is null"
        )

        self.assertIsNot(
            len(tickers) == 0,
            "ticker list is not empty"
        )

        for t in tickers:
            self.assertIsNotNone(
                t.enterprise_name,
                "ticker enterprise_name is null"
            )
            self.assertIsNotNone(
                t.sector_id,
                "ticker sector id is null"
            )
            self.assertIsNotNone(
                t.ticker_code,
                "ticker is not valid"
            )
            
        


if __name__ == '__main__':
    main()

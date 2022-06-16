from unittest import TestCase, main
from ..controllers.fundamentus_scrapper import FundamentusScrapper

class TestFundamentusScrapper(TestCase):
    def test_scrapper(self):
        scrapper = FundamentusScrapper()
        message = {
            "ticker_name":"CAML3"
        }
        price, financialstatement = scrapper.scrap(message)

        self.assertIsNotNone(
            price,
            "price is null"
        )
        
        self.assertIsNotNone(
            financialstatement,
            "financial statement is null"
        )

        print(price)
        print(financialstatement)

if __name__ == '__main__':
    main()
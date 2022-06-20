from typing import List, Dict
from ..models.use_case_processor import UseCaseProcessor
from ..controllers.messager_sender_accessor import MessagerSendAccessor
from ..controllers.infomoney_scrapper import InfomoneyScrapper
from ..models.ticker import Ticker
import json

class InfomoneyUseCase(UseCaseProcessor):
    def process(self, message: Dict):

        print('STARTING INFOMONEY SCRAPPING PROCESS')
        broker = MessagerSendAccessor.get_impl('rabbitmq')
        scrapper = InfomoneyScrapper()
        list_tickers:List[Ticker] = scrapper.scrap()

        for ticker in list_tickers:
            serialized_ticker = ticker.serialize()
            message_to_send = json.dumps(serialized_ticker)
            broker.send_message(message_to_send,'ticker')

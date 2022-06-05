from typing import Dict,List
import json
from .models.ticker import Ticker
from .controllers.scrapper_acessor import ScrapperAcessor
from .controllers.messager_sender_accessor import MessagerSendAccessor

def process(message: Dict):
    scrapping_source = message["source"]

    broker = MessagerSendAccessor.get_impl('rabbitmq')
    scrapper = ScrapperAcessor.get_impl(scrapping_source)()
    list_tickers:List[Ticker] = scrapper.scrap()
    
    for ticker in list_tickers:
        serialized_ticker = ticker.seriarize()
        message_to_send = json.dumps(serialized_ticker)
        broker.send_message(message_to_send)

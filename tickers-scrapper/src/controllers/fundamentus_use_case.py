from ..models.use_case_processor import UseCaseProcessor
from ..controllers.messager_sender_accessor import MessagerSendAccessor
from ..controllers.fundamentus_scrapper import FundamentusScrapper
from typing import Dict
import json

class FundamentusUseCase(UseCaseProcessor):
    def process(self, message: Dict):
        
        broker = MessagerSendAccessor.get_impl('rabbitmq')
        scrapper = FundamentusScrapper()
        price, financialstatement = scrapper.scrap(message)

        serialized_price = price.seriarize()
        serialized_financialstatement = financialstatement.seriarize()
        
        message_to_send = json.dumps(serialized_price)
        broker.send_message(message_to_send, 'price')
        
        message_to_send = json.dumps(serialized_financialstatement)
        broker.send_message(message_to_send, 'statement')
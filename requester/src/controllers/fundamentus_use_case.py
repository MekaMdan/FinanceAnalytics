from email.message import Message
from ..models.use_case_processor import UseCaseProcessor
from ..controllers.messager_sender_accessor import MessagerSendAccessor
from ..controllers.db_accessor import DbAccessor
import json

class FundamentusUseCase(UseCaseProcessor):
    def process(self):
        db = DbAccessor.get_impl('postgresql')
        tickers_in_db = db.get_tickers()
        broker = MessagerSendAccessor.get_impl('rabbitmq')

        for ticker in tickers_in_db:
            message = {
                "source":"fundamentus",
                "ticker_name":ticker.ticker_code
            }
            message_to_send = json.dumps(message)
            broker.send_message(message_to_send, 'scrapper')
            

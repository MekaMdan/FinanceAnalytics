from ..models.use_case_processor import UseCaseProcessor
from ..controllers.messager_sender_accessor import MessagerSendAccessor
import json

class InfomoneyUseCase(UseCaseProcessor):
    def process(self):
        message = {
            "source":"infomoney"
        }
        message_to_send = json.dumps(message)
        broker = MessagerSendAccessor.get_impl('rabbitmq')
        broker.send_message(message_to_send , 'scrapper')
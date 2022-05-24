from ..models.messager_broker_inteface import MessagerBrokerInterface
from .rabbitmq_impl import RabbitmqReceiver
from ..models.accessor_interface import AccessorInterface

class MessagerAccessor(AccessorInterface):
    messager_instance: MessagerBrokerInterface = None

    @staticmethod
    def get_impl(choosen_messager:str) -> MessagerBrokerInterface:
        available_brokers = {
            'rabbitmq':RabbitmqReceiver
        }
        if(not MessagerAccessor.messager_instance):
            MessagerAccessor.messager_instance = available_brokers[choosen_messager]()
            MessagerAccessor.messager_instance.connect_to_broker()
        return MessagerAccessor.messager_instance


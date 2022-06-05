from ..models.messager_broker_interface_send import \
    MessagerBrokerInterfaceSend
from .rabbitmq_impl_send import RabbitmqSend
from ..models.accessor_interface import AccessorInterface

class MessagerSendAccessor(AccessorInterface):
    messager_instance: MessagerBrokerInterfaceSend = None

    @staticmethod
    def get_impl(choosen_messager:str) -> MessagerBrokerInterfaceSend:
        available_brokers = {
            'rabbitmq':RabbitmqSend
        }
        if(not MessagerSendAccessor.messager_instance):
            MessagerSendAccessor.messager_instance = \
                available_brokers[choosen_messager]()
            MessagerSendAccessor.messager_instance.connect_to_broker()
        return MessagerSendAccessor.messager_instance


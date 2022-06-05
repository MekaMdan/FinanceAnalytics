from ..models.messager_broker_interface_receiver import \
    MessagerBrokerInterfaceReceiver
from .rabbitmq_impl_receiver import RabbitmqReceiver
from ..models.accessor_interface import AccessorInterface

class MessagerReceiverAccessor(AccessorInterface):
    messager_instance: MessagerBrokerInterfaceReceiver = None

    @staticmethod
    def get_impl(choosen_messager:str) -> MessagerBrokerInterfaceReceiver:
        available_brokers = {
            'rabbitmq':RabbitmqReceiver
        }
        if(not MessagerReceiverAccessor.messager_instance):
            MessagerReceiverAccessor.messager_instance = \
                available_brokers[choosen_messager]()
            MessagerReceiverAccessor.messager_instance.connect_to_broker()
        return MessagerReceiverAccessor.messager_instance


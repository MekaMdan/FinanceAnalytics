from ..process import process
from ..config import config
from ..models.messager_broker_interface_receiver import MessagerBrokerInterfaceReceiver
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
import json

class RabbitmqReceiver(MessagerBrokerInterfaceReceiver):
    connection: BlockingConnection
    channel: BlockingChannel
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect_to_broker(self):
        parameters = config('messager.ini','rabbitmq')
        connection_parameters = ConnectionParameters(
            host = parameters['host'],
            port = parameters['port'],
            virtual_host=parameters['virtual_host']
        )
        self.connection = BlockingConnection(connection_parameters)
        self.channel = self.connection.channel() 
        self.channel.basic_consume(
            queue=parameters['queue_receive'],
            on_message_callback=self.callback, 
            auto_ack=True
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
    
    def callback(self, _channel, _method, _properties, body):
        message = json.loads(body)
        process(message)

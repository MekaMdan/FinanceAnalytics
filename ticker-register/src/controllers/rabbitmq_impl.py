from ..process import process
from ..config import config
from ..models.messager_broker_inteface import MessagerBrokerInterface
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
import json

class RabbitmqReceiver(MessagerBrokerInterface):
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
            queue=parameters['queue1'],
            on_message_callback=self.callback, 
            auto_ack=True
        )
        self.channel.basic_consume(
            queue=parameters['queue2'],
            on_message_callback=self.callback, 
            auto_ack=True
        )
        self.channel.basic_consume(
            queue=parameters['queue3'],
            on_message_callback=self.callback, 
            auto_ack=True
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
    
    def callback(self, channel, method, properties, body):
        message = json.loads(body)
        process(message, method.routing_key)
        
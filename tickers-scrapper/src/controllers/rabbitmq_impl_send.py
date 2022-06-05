import json
from ..config import config
from ..models.messager_broker_interface_send import MessagerBrokerInterfaceSend
from pika import BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel

class RabbitmqSend(MessagerBrokerInterfaceSend):
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
            virtual_host=parameters['virtual_host_send']
        )
        self.connection = BlockingConnection(connection_parameters)
        self.channel = self.connection.channel()

        self.channel.queue_declare(
            queue=parameters['queue_send'],
            durable=True
            )

    def send_message(self, message_body: str):
        parameters = config('messager.ini','rabbitmq')
        self.channel.basic_publish(
            exchange=parameters['exchange_send'],
            routing_key=parameters['routing_key'],
            body=message_body
        )
        print(f'[INFO] Sent {message_body}')

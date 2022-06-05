class MessagerBrokerInterfaceSend:
    '''
    This abstract class specifies the expected methods that a messeger broker 
    Send has to implement.
    '''
    def connect_to_broker(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")

    def send_message(self, body: str):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
    
    
class MessagerBrokerInterface:
    '''
    This abstract class specifies the expected methods that a messeger broker 
    has to implement.
    '''
    def connect_to_broker(self):
        raise NotImplementedError("This method will not be implemented in this\
    abstract class")
    
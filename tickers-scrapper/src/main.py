from .controllers.messager_receiver_accessor import MessagerReceiverAccessor

def main():
    MessagerReceiverAccessor.get_impl('rabbitmq')

if __name__=="__main__":
    main()
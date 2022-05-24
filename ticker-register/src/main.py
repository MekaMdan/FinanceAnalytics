from .controllers.messager_accessor import MessagerAccessor

def main():
    MessagerAccessor.get_impl('rabbitmq')

if __name__=="__main__":
    main()

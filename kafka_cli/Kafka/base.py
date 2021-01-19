from .consumer import consumer
from .producer import producer
from .admin import admin
'''
Option 1 : Produce or consume
Option 2: topic name
Option 3: Broker
'''

class KafkaBase:
    def __init__(self,option_dict):
        self.topic = option_dict["topic"]
        self.broker = option_dict["broker"]
        self.type = option_dict["choices"]

        self.a = admin(self.broker)
        if not self.__checkTopic():
            exit()

        if self.type=="consume":
            self.con_obj = consumer(self.topic)
            if option_dict["start"]:
                self.__read()
        else:
            self.prod_obj = producer(self.topic)
            # if option_dict["start"]:
            #     self.__send()
            
        
    # def __send(self):
    #     self.prod_obj.

    def __checkTopic(self):
        return self.a.check_if_topic_present(self.topic)

    def __read(self):
        self.con_obj.start_reading()

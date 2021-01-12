from .consumer import consumer
from .producer import producer
'''
Option 1 : Produce or consume
Option 2: topic name
Option 3: Broker
'''

class KafkaBase:
    def __init_(self,*args, **kwargs):
        self.topic = kwargs["topic"]
        self.broker = kwargs["broker"]
        self.type = kwargs["choices"]
        if self.type=="consume":
            self.con_obj = consumer(self.topic,self.broker)
        else:
            self.prod_obj = producer(self.topic,self.broker)

    def read(self):
        self.con_obj.start_reading()

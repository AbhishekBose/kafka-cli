from .consumer import consumer
from .producer import producer
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
        if self.type=="consume":
            self.con_obj = consumer(self.topic)
        else:
            self.prod_obj = producer(self.topic)

    def read(self):
        self.con_obj.start_reading()

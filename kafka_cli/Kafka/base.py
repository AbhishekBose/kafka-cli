from consumer import consumer
from producer import producer

'''
Option 1 : Produce or consume
Option 2: topic name
Option 3: Broker
'''

class KafkaBase:
    def __init_(self,topic,broker="localhost:9092",con=True,prod=True):
        if con:
            self.con_obj = consumer(topic,broker)
        if prod:
            self.prod_obj = producer(topicm,broker)

    def read(self):
        self.con_obj.start_reading()

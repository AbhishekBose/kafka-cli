from confluent_kafka import Producer
import json
from .admin import admin

class producer:
    def __init__(self,topic,broker="localhost:9092",partition=None):
        self.broker = broker
        self.partition = partition
        self.prod = Producer(
            {
                'bootstrap.servers': self.broker,
            }
        )
        self.topic = topic
        self.a = admin(self.broker)

        if not self.__checkTopic():
            exit()

    def __checkTopic(self):
        return self.a.check_if_topic_present(self.topic)

    
    def __delivery_report(self,err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). 
        """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print("Message successfully delivered")
            # print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


    def produce(self,msg,json_needed=True):
        # self.prod.poll(0)
        if json_needed:
            x = json.dumps(msg)
        else:
            x =msg.encode('utf-8')
        self.prod.produce(self.topic,x,callback=self.__delivery_report)
        self.prod.poll(0)

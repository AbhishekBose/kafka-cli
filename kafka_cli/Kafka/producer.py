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
            # print("Message successfully delivered")
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


    def produce(self,msg):
        # self.prod.poll(0)
        if msg!=None or msg!="":
            updated_msg = eval(msg)
            json_message = json.dumps(updated_msg)
            try:
                self.prod.produce(self.topic,json_message,callback=self.__delivery_report)
                self.prod.poll(0)
            except Exception as e:
                print("Exception is :: {}".format(e))
            self.prod.flush(30)

# if __name__ == "__main__":
#     prod = producer("test_topic")
#     message = {"message":"hello"}
#     prod.produce(message)
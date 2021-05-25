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


    def evaluateMessage(self,msg):
        try:
            updated_msg = eval(msg)
        except NameError:
            updated_msg = msg
        return updated_msg

    def produce(self,msg):
        # self.prod.poll(0)
        if msg!=None or msg!="":
            try:
                updated_msg = self.evaluateMessage(msg)
                json_message = json.dumps(updated_msg)
                self.prod.produce(self.topic,json_message,callback=self.__delivery_report)
                self.prod.poll(0)
            except TypeError:
                print("Incorrect message format")
            except SyntaxError:
                print("Incorrect message format")
            self.prod.flush(30)

# if __name__ == "__main__":
#     prod = producer("test_topic")
#     message = {"message":"hello"}
#     prod.produce(message)
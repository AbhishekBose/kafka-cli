from .consumer import consumer
from .producer import producer
from .admin import admin
'''
Option 1 : Produce or consume
Option 2: topic name
Option 3: Broker
'''
class KafkaDetails:
    def __init__(self,broker="localhost:9092"):
        self.admin_obj = admin(self.broker)
        
    
    def getTopicList(self):
        md = self.admin_obj.a.list_topics(timeout=10)
        del(md.topics["__consumer_offsets"])
        return list(md.topics.keys())


class KafkaBase(KafkaDetails):
    def __init__(self,option_dict):
        self.data = option_dict
        self.broker = self.data["broker"]

        super().__init__(self.broker)
        # self.topic = option_dict["topic"]
        self.type = option_dict["choices"]

        #     self.prod_obj = producer(self.topic)
            # if option_dict["start"]:
            #     self.__send()
            
    def start(self,topic_data):
        if self.type=="consume":
            self.con_obj = consumer(topic_data["topic"])
            self.__read()

    # def __send(self):
    #     self.prod_obj.

    def checkTopic(self,data):
        return self.admin_obj.check_if_topic_present(data["topic"])

    def __read(self):
        self.con_obj.start_reading()

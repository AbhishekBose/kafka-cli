from .consumer import consumer
from .producer import producer
from .admin import admin
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli.log import log
import logging

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
        try:
            del(md.topics["__consumer_offsets"])
        except KeyError:
            return []
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
            
    def __start_consumer(self):
        return 1
    
    def __start_producer(self,topic_data):
        self.prod_obj = producer(topic_data["topic"])
        print("Prod object is :: {}".format(self.prod_obj))
        try:
            log("\nType your message and hit enter to send.. (Type quit to exit)","yellow")
        except Exception as e:
            logging.exception(e)
        while True:
            try:
                response = input()
                if response=="quit":
                    break
                self.prod_obj.produce(response)
            except Exception as e:
                logging.info("Exception occured during producing message")
                logging.exception(e)
            except KeyboardInterrupt:
                log("Shutting producer. Goodbye","red")
                break


    def start(self,topic_data):
        if self.type=="consume":
            self.con_obj = consumer(topic_data["topic"])
            while True:
                try:
                    time.sleep(1)
                    x= self.__read()
                    if not x:
                        continue
                        # print("Error occured. Trying to read next message")
                except KeyboardInterrupt:
                    log("\nPausing message consumption.. (Press any key to continue, type quit to exit.)","yellow")
                    try:
                        response = input()
                        if response == 'quit':
                            log("Shutting consumer. Goodbye","red")
                            break
                        log('Resuming...',"green")
                    except KeyboardInterrupt:
                        log('Resuming...',"green")
                        continue 
        
        if self.type=="produce":
            print("I am here")
            self.__start_producer(topic_data)

    # def __send(self):
    #     self.prod_obj.

    def checkTopic(self,data):
        return self.admin_obj.check_if_topic_present(data["topic"])

    def __read(self):
        x = self.con_obj.read_messages()
        return x

import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Kafka.base import KafkaBase
from .options import options
import time


def start():
    try:
        options.greet()
        opt_answers = options.opt_option()
        print(opt_answers)
        kafkaObj = KafkaBase(opt_answers)

        topic_answers = options.topic_option(kafkaObj.getTopicList())
        print(topic_answers)
        if kafkaObj.checkTopic(topic_answers):
            response = options.confirm_opt(opt_answers)
            if response["start"]:
                kafkaObj.start(topic_answers)

    except Exception:
        exit()



if __name__ == "__main__":
    start()
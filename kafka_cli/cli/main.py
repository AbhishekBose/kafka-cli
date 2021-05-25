import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Kafka.base import KafkaBase
from .options import options
import time


def start():
    exit_flag = False
    options.greet()
    try:
        while not exit_flag:
            opt_answers = options.opt_option()
            print(opt_answers)
            kafkaObj = KafkaBase(opt_answers)

            topic_answers = options.topic_option(kafkaObj.getTopicList())
            print(topic_answers)
            if kafkaObj.checkTopic(topic_answers):
                response = options.confirm_opt(opt_answers)
                if response["start"]:
                    exit_flag = kafkaObj.start(topic_answers)
                    if not exit_flag:
                        continue

    except Exception:
        exit()



if __name__ == "__main__":
    start()
import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Kafka.base import KafkaBase
from options import options


def start():
    opt_answers = options.opt_option()
    print(opt_answers)
    kafkaObj = KafkaBase(opt_answers)

    topic_answers = options.topic_option(kafkaObj.getTopicList())
    print(topic_answers)
    
if __name__ == "__main__":
    start()
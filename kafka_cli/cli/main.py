import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Kafka.base import KafkaBase
from options import options


def start():
    answers = options.option_page()
    kafkaObj = KafkaBase(answers)

if __name__ == "__main__":
    start()
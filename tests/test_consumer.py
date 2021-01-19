from .context import kafka_cli
import pytest

topic = "test_input"
con = kafka_cli.consumer.consumer(topic=topic)

def test_consumer_group():
    assert con.group == "group1"

def test_consumer_broker():
    assert con.broker == "localhost:9092"

def test_consumer_topic():
    assert con.topic == topic

# def test_subscription():
#     assert con

# def test_unknown_topic():
#     topic = "random_topic"
#     con2 = kafka_cli.consumer.consumer(topic=topic)
#     while pytest.raises(Exception):
#         assert con2.start_reading()

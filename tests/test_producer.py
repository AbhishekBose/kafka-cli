import kafka_cli
import pytest



def test_producer_broker():
    topic = "test_input"
    prod = kafka_cli.producer.producer(topic=topic)
    assert prod.broker == "localhost:9092"

def test_producer_topic():
    topic = "test_input"
    prod = kafka_cli.producer.producer(topic=topic)
    assert prod.topic == topic

def test_producer_produce(capsys):
    topic = "test_input"
    prod = kafka_cli.producer.producer(topic=topic)
    message = {"message":"message from test"}
    prod.produce(msg=message)
#     # assert 1 == 1
    out, err = capsys.readouterr()
    print("out is  :: {}".format(out))
    print("err is  :: {}".format(err))
    assert out == "Message successfully delivered"
    assert err == "Message successfully delivered"

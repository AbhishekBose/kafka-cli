from confluent_kafka import Consumer

class consumer:
    def __init__(self,broker,group,topic):
        self.broker = broker
        self.group = group
        self.con = Consumer(
            {
                'bootstrap.servers': broker,
                'group.id': group,
                'auto.offset.reset': 'earliest'
            }
        )
        self.topic = topic

        self.con.subscribe([topic])

    def start_reading(self):

        while True:
            msg = c.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            print('Received message: {}'.format(msg.value().decode('utf-8')))

    def stop(self):
        self.con.close()
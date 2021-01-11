from confluent_kafka import Consumer

class consumer:
    def __init__(self,topic,broker="localhost:9092",group="group1"):
        self.broker = broker
        self.group = group
        self.con = Consumer(
            {
                'bootstrap.servers': self.broker,
                'group.id': self.group,
                'auto.offset.reset': 'earliest'
            }
        )
        self.topic = topic

        
    def start_reading(self):
        
        # try:
        self.con.subscribe([self.topic])
        # except Exception as e:
        #     print("Original exception is :: {}".format(str(e)))
        #     raise Exception("Topic issue")

        print("Going to read messages from kafka topic {}. Press CTRL + C to stop".format(self.topic))
        while True:
            try:
                msg = self.con.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    continue

                print('Received message: {}'.format(msg.value().decode('utf-8')))
            except KeyboardInterrupt:
                print("Shutting consumer...")
                # self.stop()
                break
            except RuntimeError:
                break

    def stop(self):
        self.con.close()
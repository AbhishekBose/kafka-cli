from confluent_kafka import Consumer,KafkaError
from .admin import admin

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
        self.a = admin(self.broker)

        # if not self.__checkTopic():
        #     exit()
        self.con.subscribe([self.topic])


    def __checkTopic(self):
        return self.a.check_if_topic_present(self.topic)

        
    def read_messages(self):
        try:
            msg = self.con.poll(0.1)
            if msg is None:
                return 0
            elif msg.error():
                return 0
            print('Received message: {}'.format(msg.value().decode('utf-8')))
            return 1
        except Exception as e:
            print("Exception during reading message :: {}".format(e))
            return 0

    def start_reading(self):
        
        # try:
        # except Exception as e:
        #     print("Original exception is :: {}".format(str(e)))
        #     raise Exception("Topic issue")

        print("Going to read messages from kafka topic {}. Press CTRL + C to stop".format(self.topic))
        while True:
            try:
                msg = self.con.poll(0.1)

                if msg is None:
                    continue

                # elif msg.error().code() == KafkaError._PARTITION_EOF:
                #     print('End of partition reached {0}/{1}'
                #         .format(msg.topic(), msg.partition()))
                #     return 0
                # else:
                #     continue
                # else:
                #     print('Error occured: {0}'.format(msg.error().str()))
                #     return msg.value()

                if msg.error():
                    # print("Consumer error: {}".format(msg.error()))
                    continue

                print('Received message: {}'.format(msg.value().decode('utf-8')))
            except KeyboardInterrupt:
                print("Shutting consumer...")
                # self.stop()
                return 1
            except RuntimeError:
                break

    def stop(self):
        self.con.close()

    
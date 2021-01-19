from confluent_kafka.admin import AdminClient, NewTopic

class admin:
    def __init__(self,broker="localhost:9092"):
        self.broker = broker
        self.a = AdminClient({'bootstrap.servers': self.broker})

    def _createTopic(self,topicList,num_partitions=2,replication_factor=1):
        new_topics = [NewTopic(topic, num_partitions=num_partitions, replication_factor=replication_factor) for topic in topicList]
        fs = self.a.create_topics(new_topics)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                print("Topic {} created".format(topic))
                return 1
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))
                return 0

    def _checkTopic(self,topicName):
        md = self.a.list_topics(timeout=10)
        print(md.topics.keys())
        if topicName not in (md.topics.keys()):
            print('Topic not present')
            return 0
        else:
            return 1

    def get_topic_list(self):
        md = self.a.list_topics(timeout=10)
        del(md.topics["__consumer_offsets"])
        # print(list(md.topics.keys()))
        return list(md.topics.keys())

    def check_if_topic_present(self,topic):
        try:
            p_x= self._checkTopic(topic)
            if p_x==0:
                p_y = self._createTopic([topic])
            else:
                p_y=1
                print(topic+' already present')

        except Exception as e:
            print('Error while checking and creating topic')
            print('Error encountered is:: ',str(e))
            return 0
        # if c_y==1 and p_y==1:
        if p_y==1:
            return 1
        else:
            print('Topics werent created')
            return 0    

# if __name__ == "__main__":
#     ad = admin()
#     md = ad.a.list_topics(timeout=10)
#     del(md.topics["__consumer_offsets"])
#     print(list(md.topics.keys()))
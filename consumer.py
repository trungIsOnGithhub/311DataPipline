from kafka import KafkaConsumer

kafka_server_address = 'localhost:9092'
topic_name='stock-output-demo'

consumer = KafkaConsumer(bootstrap_servers=[kafka_server_address],
                        auto_offset_reset='latest', max_poll_records = 10)

consumer.subscribe(topics=[topic_name])
consumer.subscription()

for message in consumer:
      print ("%s:%d:%dn: key=%sn value=%sn" % (message.topic, message.partition,
                                                message.offset, message.key, message.value))
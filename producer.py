import time

from kafka import KafkaProducer

import yfinance as yf

from datetime import date

import json

current_date = date.today()

company = 'GOOG'
kafka_server_address = 'localhost:9092'
topic_name='stock-input-demo'

producer = KafkaProducer(bootstrap_servers=[kafka_server_address]) 

while True:
    data = yf.download(company, period='5d',interval='30m')

    data = data.reset_index(drop=False)

    data['Datetime'] = data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    my_dict = data.iloc[-1].to_dict()
    msg = json.dumps(my_dict)

    producer.send(topic_name, key=b'Tesla Stock Update', value=msg.encode('utf-8'))

    print(f"Producing to Topic: {topic_name}")
    time.sleep(100)
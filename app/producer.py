from kafka import KafkaProducer
import json
import requests
import time

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    return requests.get(url).json()

def send_data():
    data = get_data()

    for record in data:
        producer.send('test-topic', value=record)
        print("Sent:", record['id'])
        time.sleep(1)

if __name__ == "__main__":
    send_data()
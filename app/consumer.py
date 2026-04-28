from kafka import KafkaConsumer
import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="etl_db",
    user="postgres",
    password="Light@10",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Kafka consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening and inserting into DB...")

for message in consumer:
    data = message.value

    try:
        cur.execute(
            "INSERT INTO posts (id, title) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
            (data['id'], data['title'])
        )
        conn.commit()
        print("Inserted:", data['id'])

    except Exception as e:
        print("Error:", e)
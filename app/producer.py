import logging
from kafka import KafkaProducer
import json
import time
from app.etl.extract import extract_data

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
    api_version=(0, 10),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_data():
    try:
        data = extract_data()
        logger.info(f"Fetched {len(data)} records from API")
    except Exception as e:
        logger.error(f"Error fetching data from API: {e}")
        return

    for record in data:
        try:
            producer.send('test-topic', value=record)
            logger.info(f"Sent record ID: {record.get('id')}")
            time.sleep(1)

        except Exception as e:
            logger.error(f"Error sending record ID {record.get('id')}: {e}")

    producer.flush()
    logger.info("All records sent successfully")

if __name__ == "__main__":
    send_data()
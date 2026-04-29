import logging
from kafka import KafkaConsumer
import json
from app.etl.transform import transform_data
from app.etl.load import load_data

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='127.0.0.1:9092',
    api_version=(0, 10),
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

logger.info("Consumer started...")

batch = []

for message in consumer:
    try:
        batch.append(message.value)

        if len(batch) == 10:  # 🔥 batch size
            transformed = transform_data(batch)
            load_data(transformed)

            logger.info(f"Processed batch of {len(batch)} records")

            batch.clear()

    except Exception as e:
        logger.error(f"Error processing message: {e}")
import logging

logger = logging.getLogger(__name__)

def transform_data(data):
    transformed = []

    for item in data:
        transformed.append(
            (item['id'], item['title'].upper())
        )

    logger.info(f"Transformed {len(transformed)} records")

    return transformed
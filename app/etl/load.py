from dotenv import load_dotenv
import os
import psycopg2
import logging

load_dotenv()
logger = logging.getLogger(__name__)

def load_data(data):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        cur = conn.cursor()

        for row in data:
            cur.execute(
                "INSERT INTO posts (id, title) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
                row
            )

        conn.commit()
        logger.info(f"Inserted {len(data)} records into DB")

    except Exception as e:
        logger.error(f"Database error: {e}")

    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass
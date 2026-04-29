

#End-to-End Real-Time Data Pipeline

Overview:
This project demonstrates the design and implementation of an end-to-end real-time data pipeline using Python, Apache Kafka, and PostgreSQL. The pipeline ingests data from a REST API, streams it through Kafka, processes it in real time, and stores it in a relational database.

The project follows a modular ETL design, enabling the same components to be reused across both batch and streaming workflows.

---------------------------------

End-to-End Data Flow
The pipeline processes data through the following stages:

REST API
→ Extract (Python)
→ Kafka Producer
→ Kafka (Message Broker)
→ Kafka Consumer
→ Transform (Python)
→ Load (PostgreSQL)

----------------------------------

How It Works

1. The extract module retrieves data from an external REST API.
2. The producer sends the extracted data to a Kafka topic.
3. Kafka acts as a message broker to buffer and stream the data.
4. The consumer reads data from Kafka in real time.
5. The transform module processes and formats incoming data.
6. The load module inserts the transformed data into PostgreSQL using idempotent logic.

The consumer processes data in batches to improve performance and reduce database write overhead.

-----------------------------------

Tech Stack

Programming Language: Python
Streaming Platform: Apache Kafka
Database: PostgreSQL
Containerization: Docker
Libraries: kafka-python, psycopg2, requests, python-dotenv

-----------------------------------

Project Structure


e2e-data-pipeline/
│
├── app/
│   ├── __init__.py
│   │
│   ├── producer.py              # Kafka producer (data ingestion)
│   ├── consumer.py              # Kafka consumer (processing + load)
│   │
│   ├── etl/
│      ├── __init__.py
│      ├── extract.py            # Extract data from API
│      ├── transform.py          # Transform/clean data
│      ├── load.py               # Load data into PostgreSQL
│   
│   
│
├── docker-compose.yml           # Kafka + Zookeeper setup
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not committed)
├── .gitignore
└── README.md


---------------------------------------

Setup Instructions

1. Start Kafka and Zookeeper
   docker compose up -d

2. Start the consumer (run first)
   python -m app.consumer

3. Start the producer
   python -m app.producer

-------------------------------------

Verification

To verify the pipeline:

* Check running containers
  docker ps

* Verify data in PostgreSQL
  SELECT * FROM posts;

------------------------------------

Key Features

* Real-time data streaming using Kafka
* Modular ETL design with reusable components
* Clear separation between ingestion, processing, and storage
* Batch-based processing for improved database performance
* Idempotent inserts to prevent duplicate records
* Environment-based configuration for secure credential management
* Logging and error handling for improved reliability

-------------------------

Key Learnings

* Designing real-time data pipelines
* Understanding Kafka’s producer-consumer architecture
* Integrating streaming systems with relational databases
* Writing modular and maintainable ETL components
* Implementing error handling and logging
* Optimizing performance using batch processing

----------------------

Author: Sai Vikas Peddina
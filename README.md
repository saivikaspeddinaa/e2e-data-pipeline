# End-to-End Real-Time Data Pipeline

## 📌 Overview

This project demonstrates a real-time data pipeline using Python, Apache Kafka, and PostgreSQL. It ingests data from a REST API, streams it through Kafka, processes it in real time, and stores it in a relational database.

## 🧱 Architecture

API → Kafka Producer → Kafka → Kafka Consumer → PostgreSQL

## 🛠 Tech Stack

* Python
* Apache Kafka
* PostgreSQL
* Docker

## ⚙️ Setup Instructions

1. Start Kafka:
   docker compose up -d

2. Run Consumer:
   python app/consumer.py

3. Run Producer:
   python app/producer.py

## 🚀 Features

* Real-time data streaming using Kafka
* Modular ETL design
* Idempotent database inserts
* Containerized setup using Docker

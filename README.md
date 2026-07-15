# Marketing Data Engineering Pipeline

An end-to-end **Data Engineering Project** that simulates a real-world marketing analytics platform. This project demonstrates how data is ingested from multiple marketing systems, processed using the **Medallion Architecture (Bronze → Silver → Gold)**, orchestrated with **Apache Airflow**, stored in **MinIO**, and loaded into **PostgreSQL** for analytics.

---

# Author

**Pujita Chakraborty**

Software Engineer | Data Engineering 



---

# Project Overview

Modern organizations collect marketing data from multiple platforms such as Google Ads, Meta Ads, CRM systems, Sales applications, Email Campaigns, and Website Analytics.

This project simulates those systems using FastAPI and builds an end-to-end data pipeline to ingest, transform, and prepare analytics-ready datasets.

The project demonstrates:

- Building ETL/ELT pipelines
- Medallion Architecture
- Object Storage using MinIO
- Workflow Orchestration using Apache Airflow
- Data Warehousing using PostgreSQL
- Dockerized Development Environment

---

# Architecture

```
                         FastAPI Mock APIs
                                  │
        ┌───────────────┬──────────┴──────────┬───────────────┐
        │               │                     │               │
   Google Ads      Meta Ads               CRM System      Sales
        │               │                     │               │
        └───────────────┴──────────┬──────────┴───────────────┘
                                   │
                                   ▼
                          Bronze Layer (JSON)
                            MinIO Object Store
                                   │
                                   ▼
                         Silver Layer (Parquet)
                                   │
                                   ▼
                    Gold Layer (Business KPIs)
                                   │
                                   ▼
                     PostgreSQL Data Warehouse
                                   │
                                   ▼
                         Apache Airflow DAG
```

---

# Tech Stack

- Python
- FastAPI
- Apache Airflow
- Docker
- Docker Compose
- PostgreSQL
- MinIO
- Pandas
- SQLAlchemy
- PyArrow
- Requests
- Faker

---

# Project Structure

```
Marketing_Sales_pipeline/

│
├── bronze/
│   ├── pipeline/
│   └── storage/
│
├── silver/
│   ├── pipeline/
│   ├── storage/
│   └── transformer/
│
├── gold/
│   ├── pipeline/
│   └── storage/
│
├── warehouse/
│   └── postgres_loader.py
│
├── ingestion/
├── mock_api/
├── config/
├── dags/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Data Sources

The project simulates multiple independent marketing systems.

- Google Ads
- Meta Ads
- CRM
- Sales
- Website Analytics
- Email Campaigns
- Customer Data
- Support Tickets

---

# Medallion Architecture

## Bronze Layer

Stores raw API responses exactly as received.

Format:

- JSON

Storage:

- MinIO

Example

```
bronze/
    google_ads/
    meta_ads/
    crm/
    sales/
```

---

## Silver Layer

Cleans and standardizes the raw data.

Transformations include:

- Remove duplicate records
- Remove invalid rows
- Handle missing values
- Rename columns
- Standardize formats
- Convert JSON to Parquet

Output Format

```
Parquet
```

---

## Gold Layer

Creates business-ready datasets.

Example datasets:

- Campaign Performance
- Sales Summary
- CRM Summary
- Website Metrics
- Customer Metrics
- Email Metrics

Business KPIs include:

- CTR
- CPC
- CPA
- ROAS
- Revenue
- Cost
- Conversion Rate
- Average Order Value
- Lead Conversion Rate
- Bounce Rate
- Email Open Rate

---

# Data Flow

```
FastAPI Mock APIs

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer

↓

PostgreSQL

↓

Airflow
```

---

# Prerequisites

Install the following software before running the project:

- Docker Desktop
- Python 3.12+
- Git

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-github-username>/Marketing_Sales_pipeline.git

cd Marketing_Sales_pipeline
```

Create Virtual Environment

macOS/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Start Docker Desktop

Ensure Docker Desktop is running.

Verify

```bash
docker ps
```

---

## Step 2 — Start Infrastructure

Navigate to the Airflow project.

```bash
cd airflow-project
```

Run

```bash
docker compose up -d
```

Verify

```bash
docker ps
```

Expected containers:

- Airflow Scheduler
- Airflow Worker
- Airflow DAG Processor
- Airflow API Server
- PostgreSQL
- Redis

---

## Step 3 — Start Mock APIs

Navigate to

```bash
cd Marketing_Sales_pipeline
```

Activate environment

macOS/Linux

```bash
source .venv/bin/activate
```

Run FastAPI

```bash
python -m uvicorn mock_api.app:app --reload
```

Expected output

```
http://127.0.0.1:8000
```

Test

```
http://127.0.0.1:8000
```

Expected

```json
{
  "company": "AdVista Marketing",
  "status": "Running"
}
```

---

## Step 4 — Open Airflow

Open

```
http://localhost:8080
```

Default Credentials

Username

```
airflow
```

Password

```
airflow
```

---

## Step 5 — Open MinIO

Open

```
http://localhost:9001
```

Default Credentials

Username

```
minioadmin
```

Password

```
minioadmin
```

---

# Running the Pipeline

Open Airflow

Run DAG

```
marketing_pipeline
```

Execution Flow

```
Bronze

↓

Silver

↓

Gold

↓

Warehouse
```

---

# Testing the Project

## Test Mock API

```bash
curl http://127.0.0.1:8000
```

---

## Test Google Ads API

```bash
curl http://127.0.0.1:8000/api/google/campaigns
```

---

## Test Bronze Layer

```bash
python -c "
from ingestion.ingest_api import APIIngestion
APIIngestion().ingest('google_ads')
"
```

Expected

```
Uploading to MinIO...

bronze/google_ads/...
```

Verify in MinIO

```
bronze/
```

---

## Test Silver Layer

```bash
python -c "
from silver.pipeline.silver_pipeline import SilverPipeline
SilverPipeline().run()
"
```

Expected

```
Saved to silver/...
```

Verify in MinIO

```
silver/
```

---

## Test Gold Layer

```bash
python -c "
from gold.pipeline.gold_pipeline import GoldPipeline
GoldPipeline().run()
"
```

Expected

```
Saved to gold/...
```

Verify in MinIO

```
gold/
```

---

## Test PostgreSQL

Connect

```bash
docker exec -it marketing-postgres psql -U postgres
```

List databases

```sql
\l
```

List tables

```sql
\dt
```

Preview data

```sql
SELECT * FROM fact_sales LIMIT 10;
```

---

## Verify Airflow

Ensure all tasks complete successfully.

```
Bronze

↓

Silver

↓

Gold

↓

Warehouse
```

---

# Troubleshooting

## Airflow cannot connect to Mock API

Ensure FastAPI is running.

Inside Docker containers use

```
host.docker.internal
```

instead of

```
127.0.0.1
```

---

## MinIO Connection Error

Verify environment variables:

- MINIO_ENDPOINT
- MINIO_ACCESS_KEY
- MINIO_SECRET_KEY
- MINIO_BUCKET

---

## PostgreSQL Connection Error

Verify the PostgreSQL container is running.

```bash
docker ps
```

---

## DAG Not Appearing

Restart Airflow services

```bash
docker compose restart airflow-scheduler airflow-dag-processor
```

---

# Future Improvements

- Incremental Data Loading
- Data Validation
- Great Expectations
- dbt
- Apache Spark
- Snowflake
- AWS S3 Integration
- CI/CD Pipeline
- Unit Testing
- Monitoring & Alerting

---

# Learning Outcomes

This project demonstrates practical experience with:

- Designing ETL/ELT pipelines
- Medallion Architecture
- Apache Airflow DAG orchestration
- Object Storage using MinIO
- Building REST APIs with FastAPI
- Data transformation using Pandas
- Parquet data storage
- PostgreSQL Data Warehousing
- Dockerized development environments
- End-to-end Data Engineering workflows

---

# License

This project is created for educational and portfolio purposes.

---

## Thank You

If you found this project useful, feel free to ⭐ the repository and connect with me on GitHub.

**Author:** **Pujita Chakraborty**

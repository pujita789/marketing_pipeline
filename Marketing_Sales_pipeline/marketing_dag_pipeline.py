import os
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add the project root to the path so Airflow can import our packages
# (bronze, silver, gold, warehouse, config) regardless of where the
# DAGs folder lives.
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from bronze.pipeline.bronze_pipeline import BronzePipeline
from silver.pipeline.silver_pipeline import SilverPipeline
from gold.pipeline.gold_pipeline import GoldPipeline
from warehouse.warehouse_pipeline import WarehousePipeline
from config.logger import get_logger

logger = get_logger(__name__)


def run_bronze(**context):

    logger.info("Starting Bronze Layer...")

    try:
        BronzePipeline().run()

        logger.info("Bronze Layer completed successfully.")

    except Exception as e:
        logger.error(f"Bronze Layer failed: {e}")
        raise


def run_silver(**context):

    logger.info("Starting Silver Layer...")

    try:
        SilverPipeline().run()

        logger.info("Silver Layer completed successfully.")

    except Exception as e:
        logger.error(f"Silver Layer failed: {e}")
        raise


def run_gold(**context):

    logger.info("Starting Gold Layer...")

    try:
        GoldPipeline().run()

        logger.info("Gold Layer completed successfully.")

    except Exception as e:
        logger.error(f"Gold Layer failed: {e}")
        raise


def run_warehouse(**context):

    logger.info("Starting Warehouse Load...")

    try:
        WarehousePipeline().run()

        logger.info("Warehouse Load completed successfully.")

    except Exception as e:
        logger.error(f"Warehouse Load failed: {e}")
        raise


default_args = {
    "owner": "data-engineering",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="marketing_sales_pipeline",
    description="Bronze -> Silver -> Gold -> Warehouse marketing pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["marketing", "bronze", "silver", "gold", "warehouse"],
) as dag:

    bronze_task = PythonOperator(
        task_id="bronze_layer",
        python_callable=run_bronze,
    )

    silver_task = PythonOperator(
        task_id="silver_layer",
        python_callable=run_silver,
    )

    gold_task = PythonOperator(
        task_id="gold_layer",
        python_callable=run_gold,
    )

    warehouse_task = PythonOperator(
        task_id="warehouse_load",
        python_callable=run_warehouse,
    )

    bronze_task >> silver_task >> gold_task >> warehouse_task

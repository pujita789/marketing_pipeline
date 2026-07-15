import time
import requests

from bronze.storage.bronze_storage import BronzeStorage
from config.sources import SOURCES
from config.logger import get_logger

logger = get_logger(__name__)


class APIIngestion:

    def __init__(self):
        self.storage = BronzeStorage()

    def ingest(self, source):

        config = SOURCES[source]

        start = time.perf_counter()

        logger.info(f"Calling API: {config['url']}")
        t1 = time.perf_counter()

        response = requests.get(config["url"])

        t2 = time.perf_counter()

        logger.info(f"Status: {response.status_code}")
        response.raise_for_status()

        data = response.json()
        t3 = time.perf_counter()

        logger.info("Uploading to MinIO...")
        records = data[config["response_key"]]

        path = self.storage.save_json(
            source=source,
            data=records
        )

        t4 = time.perf_counter()

        logger.info(
            f"API Call: {t2-t1:.3f}s | "
            f"JSON Parsing: {t3-t2:.3f}s | "
            f"MinIO Upload: {t4-t3:.3f}s | "
            f"Total: {t4-start:.3f}s"
        )

        logger.info(f"Saved to {path}")

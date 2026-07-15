from config.sources import SOURCES
from ingestion.ingest_api import APIIngestion
from config.logger import get_logger

logger = get_logger(__name__)


class BronzePipeline:

    def __init__(self):
        self.ingestion = APIIngestion()

    def run(self):

        for source in SOURCES:

            logger.info(f"Ingesting {source}...")

            try:
                self.ingestion.ingest(source)

                logger.info(f"{source} completed.")

            except Exception as e:
                raise Exception(f"Bronze ingestion failed for {source}: {e}")
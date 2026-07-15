from gold.storage.gold_storage import GoldStorage
from warehouse.postgres_loader import PostgreSQLLoader
from config.logger import get_logger

logger = get_logger(__name__)


class WarehousePipeline:

    def __init__(self):

        self.storage = GoldStorage()

        self.loader = PostgreSQLLoader()

    def process(self, dataset):

        logger.info(f"Loading {dataset} into PostgreSQL...")

        df = self.storage.read_latest_gold(dataset)

        self.loader.load(

            dataframe=df,

            table_name=dataset

        )

    def run(self):

        datasets = [

            "campaign_performance",

            "customer_analytics",

            "support_analytics",

            "executive_dashboard"

        ]

        for dataset in datasets:

            try:
                self.process(dataset)

                logger.info(f"{dataset} loaded.")

            except Exception as e:
                raise Exception(f"Warehouse load failed for {dataset}: {e}")

        logger.info("Warehouse Loaded Successfully!")

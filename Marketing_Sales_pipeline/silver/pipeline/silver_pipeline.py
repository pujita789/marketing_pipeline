import pandas as pd

from silver.storage.silver_storage import SilverStorage

from transformations.google_transform import GoogleTransformer
from transformations.meta_transform import MetaTransformer
from transformations.crm_transform import CRMTransformer
from transformations.sales_transform import SalesTransformer
from transformations.website_transform import WebsiteTransformer
from transformations.support_transform import SupportTransformer
from transformations.customer_transform import CustomerTransformer

from config.logger import get_logger

logger = get_logger(__name__)


class SilverPipeline:

    def __init__(self):

        self.storage = SilverStorage()

        self.transformers = {

            "google_ads": GoogleTransformer(),

            "meta_ads": MetaTransformer(),

            "crm": CRMTransformer(),

            "sales_ads": SalesTransformer(),

            "website": WebsiteTransformer(),

            "support": SupportTransformer(),

            "customers": CustomerTransformer()

        }

    def process(self, source: str):

        logger.info(f"Processing {source}...")

        # Read latest Bronze file
        df = self.storage.read_latest_bronze(source)

        logger.info(f"Rows read : {len(df)}")

        # Get transformer
        transformer = self.transformers.get(source)

        if transformer is None:
            raise Exception(
                f"No transformer found for {source}"
            )

        # Clean data
        clean_df = transformer.transform(df)

        logger.info(f"Rows after cleaning : {len(clean_df)}")

        # Save into Silver
        path = self.storage.save_parquet(

            source=source,

            df=clean_df

        )

        logger.info(f"Saved to {path}")

        return path

    def run(self):

        for source in self.transformers.keys():

            try:
                self.process(source)

                logger.info(f"{source} completed.")

            except Exception as e:
                raise Exception(f"Silver processing failed for {source}: {e}")

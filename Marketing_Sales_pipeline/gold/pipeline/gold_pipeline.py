from gold.storage.gold_storage import GoldStorage
from gold.transformations.transformation_factory import GoldTransformationFactory
from config.logger import get_logger

logger = get_logger(__name__)


class GoldPipeline:

    def __init__(self):

        self.storage = GoldStorage()

    # ---------------------------------------------------------
    # Campaign Performance
    # ---------------------------------------------------------

    def process_campaign_performance(self):

        logger.info("Building Campaign Performance Dataset...")

        google_df = self.storage.read_latest_silver("google_ads")
        meta_df = self.storage.read_latest_silver("meta_ads")
        sales_df = self.storage.read_latest_silver("sales_ads")
        crm_df = self.storage.read_latest_silver("crm")

        transformer = GoldTransformationFactory.get_transformation(
            "campaign_performance"
        )

        gold_df = transformer.transform(
            google_df,
            meta_df,
            sales_df,
            crm_df
        )

        path = self.storage.save_parquet(
            "campaign_performance",
            gold_df
        )

        logger.info(f"Saved Gold Dataset : {path}")

    # ---------------------------------------------------------
    # Customer Analytics
    # ---------------------------------------------------------

    def process_customer_analytics(self):

        logger.info("Building Customer Analytics Dataset...")

        customers_df = self.storage.read_latest_silver("customers")
        sales_df = self.storage.read_latest_silver("sales_ads")
        crm_df = self.storage.read_latest_silver("crm")

        transformer = GoldTransformationFactory.get_transformation(
            "customer_analytics"
        )

        gold_df = transformer.transform(
            customers_df,
            sales_df,
            crm_df
        )

        path = self.storage.save_parquet(
            "customer_analytics",
            gold_df
        )

        logger.info(f"Saved Gold Dataset : {path}")

    # ---------------------------------------------------------
    # Support Analytics
    # ---------------------------------------------------------

    def process_support_analytics(self):

        logger.info("Building Support Analytics Dataset...")

        support_df = self.storage.read_latest_silver("support")
        customers_df = self.storage.read_latest_silver("customers")

        transformer = GoldTransformationFactory.get_transformation(
            "support_analytics"
        )

        gold_df = transformer.transform(
            support_df,
            customers_df
        )

        path = self.storage.save_parquet(
            "support_analytics",
            gold_df
        )

        logger.info(f"Saved Gold Dataset : {path}")

    # ---------------------------------------------------------
    # Executive Dashboard
    # ---------------------------------------------------------

    def process_executive_dashboard(self):

        logger.info("Building Executive Dashboard Dataset...")

        campaign_df = self.storage.read_latest_gold(
            "campaign_performance"
        )

        customer_df = self.storage.read_latest_gold(
            "customer_analytics"
        )

        support_df = self.storage.read_latest_gold(
            "support_analytics"
        )

        website_df = self.storage.read_latest_silver(
            "website"
        )

        transformer = GoldTransformationFactory.get_transformation(
            "executive_dashboard"
        )

        gold_df = transformer.transform(
            campaign_df,
            customer_df,
            support_df,
            website_df
        )

        path = self.storage.save_parquet(
            "executive_dashboard",
            gold_df
        )

        logger.info(f"Saved Gold Dataset : {path}")

    # ---------------------------------------------------------
    # Run All Gold Pipelines
    # ---------------------------------------------------------

    def run(self):

        steps = [
            ("campaign_performance", self.process_campaign_performance),
            ("customer_analytics", self.process_customer_analytics),
            ("support_analytics", self.process_support_analytics),
            ("executive_dashboard", self.process_executive_dashboard),
        ]

        for name, step in steps:

            try:
                step()

                logger.info(f"{name} completed.")

            except Exception as e:
                raise Exception(f"Gold processing failed for {name}: {e}")

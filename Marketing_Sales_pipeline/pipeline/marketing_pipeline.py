from bronze.pipeline.bronze_pipeline import BronzePipeline
from silver.pipeline.silver_pipeline import SilverPipeline
from gold.pipeline.gold_pipeline import GoldPipeline
from warehouse.warehouse_pipeline import WarehousePipeline
from config.logger import get_logger

logger = get_logger(__name__)


def main():

    logger.info("=" * 60)
    logger.info("BRONZE LAYER")
    logger.info("=" * 60)

    try:
        BronzePipeline().run()
        logger.info("Bronze Layer Completed Successfully")

    except Exception as e:
        logger.error(f"Bronze Layer Failed: {e}")
        logger.error("Pipeline Aborted.")
        return

    logger.info("=" * 60)
    logger.info("SILVER LAYER")
    logger.info("=" * 60)

    try:
        SilverPipeline().run()
        logger.info("Silver Layer Completed Successfully")

    except Exception as e:
        logger.error(f"Silver Layer Failed: {e}")
        logger.error("Pipeline Aborted.")
        return

    logger.info("=" * 60)
    logger.info("GOLD LAYER")
    logger.info("=" * 60)

    try:
        GoldPipeline().run()
        logger.info("Gold Layer Completed Successfully")

    except Exception as e:
        logger.error(f"Gold Layer Failed: {e}")
        logger.error("Pipeline Aborted.")
        return

    logger.info("=" * 60)
    logger.info("WAREHOUSE LAYER")
    logger.info("=" * 60)

    try:
        WarehousePipeline().run()
        logger.info("Warehouse Layer Completed Successfully")

    except Exception as e:
        logger.error(f"Warehouse Layer Failed: {e}")
        logger.error("Pipeline Aborted.")
        return

    logger.info("=" * 60)
    logger.info("COMPLETE PIPELINE EXECUTED SUCCESSFULLY")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()

from io import BytesIO
from datetime import datetime

import pandas as pd
from minio import Minio

from config.settings import settings
from config.logger import get_logger

logger = get_logger(__name__)


class GoldStorage:

    def __init__(self):

        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )

        self.silver_bucket = "silver"
        self.gold_bucket = "gold"

    def ensure_bucket_exists(self):

        if not self.client.bucket_exists(self.gold_bucket):
            self.client.make_bucket(self.gold_bucket)
            logger.info(f"Created bucket: {self.gold_bucket}")

    # -----------------------------------------------------
    # Generic Reader
    # layer -> silver / gold
    # -----------------------------------------------------

    def read_latest(self, layer: str, dataset: str) -> pd.DataFrame:

        bucket = self.silver_bucket if layer == "silver" else self.gold_bucket

        prefix = f"{layer}/{dataset}/"

        objects = list(
            self.client.list_objects(
                bucket,
                prefix=prefix,
                recursive=True
            )
        )

        if not objects:
            raise Exception(
                f"No {layer} data found for {dataset}"
            )

        latest_object = max(
            objects,
            key=lambda obj: obj.last_modified
        )

        response = self.client.get_object(
            bucket,
            latest_object.object_name
        )

        parquet_bytes = BytesIO(
            response.read()
        )

        response.close()
        response.release_conn()

        df = pd.read_parquet(parquet_bytes)

        logger.info(f"Loaded {layer}/{dataset}: {len(df)} rows")

        return df

    # -----------------------------------------------------
    # Wrapper Methods
    # -----------------------------------------------------

    def read_latest_silver(self, dataset):

        return self.read_latest(
            "silver",
            dataset
        )

    def read_latest_gold(self, dataset):

        return self.read_latest(
            "gold",
            dataset
        )

    # -----------------------------------------------------
    # Save Gold Dataset
    # -----------------------------------------------------

    def save_parquet(
        self,
        dataset_name,
        df
    ):

        self.ensure_bucket_exists()

        now = datetime.now()

        object_name = (

            f"gold/"
            f"{dataset_name}/"
            f"year={now:%Y}/"
            f"month={now:%m}/"
            f"day={now:%d}/"
            f"{dataset_name}_{now:%Y%m%d_%H%M%S}.parquet"

        )

        buffer = BytesIO()

        df.to_parquet(
            buffer,
            engine="pyarrow",
            index=False
        )

        buffer.seek(0)

        self.client.put_object(

            bucket_name=self.gold_bucket,

            object_name=object_name,

            data=buffer,

            length=buffer.getbuffer().nbytes,

            content_type="application/octet-stream"

        )

        logger.info(f"Saved Gold Dataset -> {object_name}")

        return object_name

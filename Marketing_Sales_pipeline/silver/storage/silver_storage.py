from io import BytesIO
from datetime import datetime

import json
import pandas as pd

from minio import Minio

from config.settings import settings
from config.logger import get_logger

logger = get_logger(__name__)


class SilverStorage:

    def __init__(self):

        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )

        self.bronze_bucket = settings.MINIO_BUCKET
        self.silver_bucket = "silver"

    def ensure_bucket_exists(self):

        if not self.client.bucket_exists(self.silver_bucket):
            self.client.make_bucket(self.silver_bucket)
            logger.info(f"Created bucket: {self.silver_bucket}")

    def read_latest_bronze(self, source: str) -> pd.DataFrame:

        prefix = f"bronze/{source}/"

        objects = list(
            self.client.list_objects(
                self.bronze_bucket,
                prefix=prefix,
                recursive=True
            )
        )

        if not objects:
            raise Exception(
                f"No Bronze files found for {source}"
            )

        latest_object = max(
            objects,
            key=lambda obj: obj.last_modified
        )

        response = self.client.get_object(
            self.bronze_bucket,
            latest_object.object_name
        )

        data = json.loads(
            response.read().decode("utf-8")
        )

        response.close()
        response.release_conn()

        logger.info(f"Read Bronze file: {latest_object.object_name}")

        return pd.DataFrame(data)

    def save_parquet(
        self,
        source: str,
        df: pd.DataFrame
    ):

        self.ensure_bucket_exists()

        now = datetime.now()
        object_name = (
            f"silver/"
            f"{source}/"
            f"year={now:%Y}/"
            f"month={now:%m}/"
            f"day={now:%d}/"
            f"{source}_{now:%Y%m%d_%H%M%S}.parquet"
        )

        parquet_buffer = BytesIO()

        df.to_parquet(
            parquet_buffer,
            index=False,
            engine="pyarrow"
        )
        parquet_buffer.seek(0)

        self.client.put_object(
            bucket_name=self.silver_bucket,
            object_name=object_name,
            data=parquet_buffer,
            length=parquet_buffer.getbuffer().nbytes,
            content_type="application/octet-stream"
        )

        logger.info(f"Saved to {object_name}")

        return object_name

import json
from io import BytesIO
from datetime import datetime

from minio import Minio

from config.settings import settings
from config.logger import get_logger

logger = get_logger(__name__)


class BronzeStorage:

    def __init__(self):

        self.client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False
        )

        self.bucket = settings.MINIO_BUCKET

    def ensure_bucket_exists(self):

        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)
            logger.info(f"Created bucket: {self.bucket}")

    def save_json(self, source: str, data):

        self.ensure_bucket_exists()

        now = datetime.now()

        object_name = (
            f"bronze/"
            f"{source}/"
            f"year={now:%Y}/"
            f"month={now:%m}/"
            f"day={now:%d}/"
            f"{source}_{now:%Y%m%d_%H%M%S}.json"
        )

        json_bytes = json.dumps(
            data,
            indent=4
        ).encode("utf-8")

        self.client.put_object(
            bucket_name=self.bucket,
            object_name=object_name,
            data=BytesIO(json_bytes),
            length=len(json_bytes),
            content_type="application/json"
        )

        return object_name
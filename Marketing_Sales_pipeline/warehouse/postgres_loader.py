from sqlalchemy import create_engine
import pandas as pd

from warehouse.config import DB_CONFIG
from config.logger import get_logger

logger = get_logger(__name__)


class PostgreSQLLoader:

    def __init__(self):

        self.engine = create_engine(

            f"postgresql+psycopg2://"
            f"{DB_CONFIG['username']}:"
            f"{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:"
            f"{DB_CONFIG['port']}/"
            f"{DB_CONFIG['database']}"

        )

    def load(
        self,
        dataframe: pd.DataFrame,
        table_name: str
    ):

        logger.info(f"Loading {table_name}...")

        try:
            dataframe.to_sql(

                name=table_name,
                con=self.engine,
                if_exists="replace",
                index=False,
                method="multi",
                chunksize=1000

            )

        except Exception as e:
            raise Exception(f"Failed to load {table_name} into PostgreSQL: {e}")

        logger.info(f"Loaded {len(dataframe)} rows into {table_name}")

from sqlalchemy import create_engine

from warehouse.config import DB_CONFIG


engine = create_engine(

    f"postgresql+psycopg2://"

    f"{DB_CONFIG['username']}:"

    f"{DB_CONFIG['password']}@"

    f"{DB_CONFIG['host']}:"

    f"{DB_CONFIG['port']}/"

    f"{DB_CONFIG['database']}"

)

with engine.connect() as conn:

    print("✅ Connected Successfully")
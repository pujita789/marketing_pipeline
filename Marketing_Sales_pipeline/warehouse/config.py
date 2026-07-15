from config.settings import settings


DB_CONFIG = {

    "host": settings.POSTGRES_HOST,

    "port": settings.POSTGRES_PORT,

    "database": settings.POSTGRES_DB,

    "username": settings.POSTGRES_USER,

    "password": settings.POSTGRES_PASSWORD

}

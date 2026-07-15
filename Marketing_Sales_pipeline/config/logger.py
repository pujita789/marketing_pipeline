import logging


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger.
    Reused by Bronze, Silver, Gold and Warehouse layers so every
    layer logs in the same format.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger

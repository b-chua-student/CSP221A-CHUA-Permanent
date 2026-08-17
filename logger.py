import logging
import functools
import os

def log_action(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info(f"Starting {func.__name__}")
        result = func(self, *args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return result
    return wrapper

def ensure_log_directories(path: str = "logs") -> None:
    os.makedirs(path, exist_ok=True)

def configure_logging(filename: str, logger_name: str | None = None, level: int = logging.INFO, fmt: str = "%(asctime)s - %(levelname)s - %(message)s") -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.propagate = False # avoid duplicate logs to root logger

    handler = logging.FileHandler(filename, mode="w")
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)

    return logger




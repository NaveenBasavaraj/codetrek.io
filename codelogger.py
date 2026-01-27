import logging
from logging.handlers import TimedRotatingFileHandler
import time
from datetime import datetime
import os

def setup():
    logger = logging.getLogger("code_logger")
    logger.setLevel(logging.DEBUG)

    log_folder = "/workspaces/codtrek.io/logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_handler = TimedRotatingFileHandler(
        f"{log_folder}/debug_logs_{current_date}.log",
        when="midnight", 
        interval=1,
        backupCount=7,
    )

    log_format = "%(asctime)s - [%(levelname)s] - %(name)s - %(funcName)s - %(message)s"
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # Console handler for real-time logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

def log_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger = logging.getLogger("code_logger")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(str(e))
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(f"Executed function '{func.__name__}' in {execution_time:.4f} seconds")
    return wrapper



logger = setup()
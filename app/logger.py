import logging
import os
import uuid
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler



# CREATE LOG DIRECTORY

if not os.path.exists("logs"):
    os.makedirs("logs")



# LOG FILE (DAILY ROTATION)

LOG_FILE = f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"



# REQUEST ID FILTER

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "request_id"):
            record.request_id = "N/A"
        return True



# FORMATTER (STRUCTURED)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(request_id)s | %(name)s | %(message)s"
)



# FILE HANDLER (ROTATING LOGS)

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,  # 5MB
    backupCount=3
)
file_handler.setFormatter(formatter)



# CONSOLE HANDLER

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)



# LOGGER INSTANCE

logger = logging.getLogger("task-api")
logger.setLevel(logging.INFO)

logger.addFilter(RequestIdFilter())

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)



# LOGGER WITH REQUEST ID

def get_logger_with_request_id(request_id: str):
    return logging.LoggerAdapter(logger, {"request_id": request_id})



# OPTIONAL: REQUEST TIMER HELPER

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        logger.info(
            f"Execution Time | {func.__name__} | {end_time - start_time:.3f}s"
        )
        return result

    return wrapper
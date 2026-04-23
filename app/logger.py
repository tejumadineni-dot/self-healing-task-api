import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
import uuid


# CREATE LOGS DIRECTORY

if not os.path.exists("logs"):
    os.makedirs("logs")


# LOG FILE

LOG_FILE = f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"

# FORMAT WITH REQUEST ID 

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "request_id"):
            record.request_id = "N/A"
        return True


formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(request_id)s | %(name)s | %(message)s"
)


# FILE HANDLER

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=3
)
file_handler.setFormatter(formatter)


# CONSOLE HANDLER

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


# LOGGER

logger = logging.getLogger("self-healing-api")
logger.setLevel(logging.INFO)

logger.addFilter(RequestIdFilter())

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)



# HELPER TO ATTACH REQUEST ID

def get_logger_with_request_id(request_id: str):
    return logging.LoggerAdapter(logger, {"request_id": request_id})
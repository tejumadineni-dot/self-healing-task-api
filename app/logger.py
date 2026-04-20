import logging
import os
from datetime import datetime

# create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

LOG_FILE = f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("self-healing-api")
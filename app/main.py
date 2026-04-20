from fastapi import FastAPI
from app.routes import router
from app.logger import logger

app = FastAPI()

app.include_router(router)

logger.info("App started")
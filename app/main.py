from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid

from app.routes import router
from app.database.db import engine, Base
from app.logger import logger, get_logger_with_request_id

app = FastAPI(
    title="Task Management API",
    description="Self-Healing API with Logging & Retry Mechanism",
    version="1.0.0"
)

# CREATE DB TABLES

Base.metadata.create_all(bind=engine)


# INCLUDE ROUTES

app.include_router(router)

logger.info(" Application started")



# GLOBAL EXCEPTION HANDLER

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    req_logger = getattr(request.state, "logger", logger) #safe logger usage

    req_logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong"}
    )



# REQUEST LOGGING MIDDLEWARE 

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Unique Request ID
    request_id = str(uuid.uuid4())

    # Attach logger with request_id
    request.state.logger = get_logger_with_request_id(request_id)

    request.state.logger.info(f"Incoming request: {request.method} {request.url}")

    try:
        response = await call_next(request)
    except Exception as e:
        request.state.logger.error(f"Request failed: {str(e)}")
        raise e

    request.state.logger.info(f"Response status: {response.status_code}")

    return response
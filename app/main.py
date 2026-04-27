from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid
import time

from app.routes import router
from app.database.db import engine, Base
from app.logger import logger, get_logger_with_request_id



# FASTAPI APP INIT

app = FastAPI(
    title="Task Management API",
    description="Self-Healing API with Logging, Retry Mechanism, and Service Layer Architecture",
    version="1.0.0"
)


# CREATE DATABASE TABLES

Base.metadata.create_all(bind=engine)



# INCLUDE ROUTES

app.include_router(router)


logger.info("Application started successfully")



# GLOBAL EXCEPTION HANDLER

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    req_logger = getattr(request.state, "logger", logger)

    req_logger.error(f"Unhandled Exception: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )



# REQUEST LOGGING MIDDLEWARE

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    # Unique Request ID
    request_id = str(uuid.uuid4())

    # Attach logger with request ID
    request.state.logger = get_logger_with_request_id(request_id)

    request.state.logger.info(
        f"START | {request.method} {request.url}"
    )

    try:
        response = await call_next(request)

    except Exception as e:
        request.state.logger.error(f"Request Failed: {str(e)}")
        raise e

    process_time = time.time() - start_time

   
    request.state.logger.info(f"END | STATUS={response.status_code} | TIME={process_time:.3f}s")

    return response
import time
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from app.database.deps import get_db
from app.database.models import TaskDB
from app.schemas import Task, TaskResponse
from app.services.task_service import (
    create_task_service,
    get_tasks_service,
    update_task_service,
    delete_task_service
)

router = APIRouter()



# RETRY MECHANISM (DB SAFE)

def retry_db_operation(func, logger, retries=3, delay=1):
    for attempt in range(retries):
        try:
            return func()
        except SQLAlchemyError as e:
            logger.error(f"Attempt {attempt + 1} failed | {str(e)}")
            time.sleep(delay * (2 ** attempt))

    raise HTTPException(
        status_code=500,
        detail="Database operation failed after retries"
    )



# HEALTH CHECK

@router.get("/health")
def health_check(request: Request, db: Session = Depends(get_db)):
    logger = request.state.logger

    try:
        db.execute(text("SELECT 1"))
        logger.info("Health check successful")
        return {"status": "healthy"}

    except Exception as e:
        logger.error(f"Health check failed | {str(e)}")
        raise HTTPException(status_code=500, detail="DB Down")



# CREATE TASK

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: Task, request: Request, db: Session = Depends(get_db)):
    logger = request.state.logger
    logger.info("Creating task")

    return retry_db_operation(
        lambda: create_task_service(task, db, logger),
        logger
    )



# GET TASKS (PAGINATION)

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Fetching tasks | skip={skip} | limit={limit}")

    return retry_db_operation(
        lambda: get_tasks_service(db, skip, limit, logger),
        logger
    )



# UPDATE TASK

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: Task,
    request: Request,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Updating task | ID={task_id}")

    return retry_db_operation(
        lambda: update_task_service(task_id, task, db, logger),
        logger
    )



# DELETE TASK

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Deleting task | ID={task_id}")

    return retry_db_operation(
        lambda: delete_task_service(task_id, db, logger),
        logger
    )
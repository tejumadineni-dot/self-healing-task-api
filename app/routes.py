import time
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from app.database.deps import get_db
from app.database.models import TaskDB
from app.schemas import Task, TaskResponse

router = APIRouter()



# SELF-HEALING RETRY 

def retry_db_operation(func, logger, retries=3, delay=1):
    for attempt in range(retries):
        try:
            return func()
        except SQLAlchemyError as e:
            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
            time.sleep(delay * (2 ** attempt))  # exponential backoff

    raise HTTPException(status_code=500, detail="DB operation failed after retries")



# HEALTH CHECK 

@router.get("/health")
def health_check(request: Request, db: Session = Depends(get_db)):
    logger = request.state.logger

    try:
        db.execute(text("SELECT 1"))
        logger.info("Health check successful")
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Database Down")


# CREATE TASK

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task, request: Request, db: Session = Depends(get_db)):
    logger = request.state.logger
    logger.info("Creating task")

    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    def db_action():
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    return retry_db_operation(db_action, logger)

# GET TASKS (Pagination )

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Fetching tasks | skip={skip}, limit={limit}")

    try:
        tasks = db.query(TaskDB).offset(skip).limit(limit).all()
        return tasks
    except Exception as e:
        logger.error(f"Error fetching tasks: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



# UPDATE TASK

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: Task,
    request: Request,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Updating task {task_id}")

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.warning(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed

    def db_action():
        db.commit()
        db.refresh(db_task)
        return db_task

    return retry_db_operation(db_action, logger)



# DELETE TASK

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    logger = request.state.logger
    logger.info(f"Deleting task {task_id}")

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.warning(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")

    def db_action():
        db.delete(db_task)
        db.commit()
        return {
            "status": "success",
            "message": "Task deleted successfully",
            "task_id": task_id
        }

    return retry_db_operation(db_action, logger)
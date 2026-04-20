from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.database.models import TaskDB
from app.schemas import Task, TaskResponse
from app.logger import logger

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: Task, db: Session = Depends(get_db)):

    logger.info("Creating task")

    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return new_task


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):

    logger.info("Fetching tasks")

    return db.query(TaskDB).all()


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.error("Task not found")
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed

    try:
        db.commit()
        db.refresh(db_task)
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return db_task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.error("Task not found")
        raise HTTPException(status_code=404, detail="Task not found")

    try:
        db.delete(db_task)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting task: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {
        "status": "success",
        "message": "Task deleted successfully",
        "task_id": task_id
    }
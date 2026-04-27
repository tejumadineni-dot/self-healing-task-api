from app.database.models import TaskDB
from fastapi import HTTPException


#  CREATE TASK
def create_task_service(task, db, logger):
    logger.info("Service: Creating task")

    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


#  GET TASKS (Pagination)
def get_tasks_service(db, skip, limit, logger):
    logger.info(f"Service: Fetching tasks | skip={skip}, limit={limit}")

    try:
        tasks = db.query(TaskDB).offset(skip).limit(limit).all()
        return tasks

    except Exception as e:
        logger.error(f"Error fetching tasks: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

#  UPDATE TASK
def update_task_service(task_id, task, db, logger):
    logger.info(f"Service: Updating task {task_id}")

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.warning(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed

    db.commit()
    db.refresh(db_task)

    return db_task


#  DELETE TASK
def delete_task_service(task_id, db, logger):
    logger.info(f"Service: Deleting task {task_id}")

    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()

    if not db_task:
        logger.warning(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()

    return {
        "status": "success",
        "message": "Task deleted successfully",
        "task_id": task_id
    }
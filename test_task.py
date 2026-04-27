from app.services.task_service import create_task_service
from app.schemas import Task

# dummy db (temporary)
class DummyDB:
    def add(self, x): pass
    def commit(self): pass
    def refresh(self, x): pass

# dummy logger
class DummyLogger:
    def info(self, msg): pass

def test_create_task():
    task = Task(
        title="Test Task",
        description="Testing",
        completed=False
    )

    db = DummyDB()
    logger = DummyLogger()

    result = create_task_service(task, db, logger)

    assert result.title == "Test Task"
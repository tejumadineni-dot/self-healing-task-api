from app.database.db import SessionLocal

#  DATABASE DEPENDENCY (DB SESSION PROVIDER)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
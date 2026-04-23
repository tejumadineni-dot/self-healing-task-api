from app.database.db import SessionLocal

#  Dependency (DB session provider)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
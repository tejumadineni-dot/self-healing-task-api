from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False,index=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
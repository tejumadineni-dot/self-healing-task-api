from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

# TASK TABLE MODEL

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)     #UNIQUE TASK IDENTIFIER
    title = Column(String(100), nullable=False)            #TASK HEADING 
    description = Column(String(500), nullable=False)      #TASK DETAILS
    completed = Column(Boolean, default=False)             #TASK DONE
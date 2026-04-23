from pydantic import BaseModel, Field

#  Request Schema (input validation)
class Task(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5,max_length=500)
    completed: bool = False


#  Response Schema (output format)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True   # SQLAlchemy support
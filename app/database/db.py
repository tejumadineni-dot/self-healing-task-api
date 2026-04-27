from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

#DATABASE ENGINE

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#SESSION LOCAL

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

#BASE CLASS

Base = declarative_base()
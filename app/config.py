from pydantic_settings import BaseSettings


# APPLICATION SETTINGS

class Settings(BaseSettings):

    # Database URL 
    DATABASE_URL: str = "sqlite:///./task.db"

    # App settings
    APP_NAME: str = "Task Management API"
    DEBUG: bool = True

    # Logging level
    LOG_LEVEL: str = "INFO"



# LOAD SETTINGS

settings = Settings()
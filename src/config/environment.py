from pydantic_settings import BaseSettings

class Environment(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_DB: str 


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_environment():
    return Environment()
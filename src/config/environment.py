from pydantic.settings import BaseSettings

class environment(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# create fucntion that return the envirment settings

def get_environment():
    return environment()
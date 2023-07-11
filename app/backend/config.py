# config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME = "Default"  # default value if env variable does not exist

# specify .env file location as Config attribute
    class Config:
        env_file = "../.env"

# global instance
settings = Settings()

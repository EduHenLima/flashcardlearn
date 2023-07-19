import os

from dotenv import load_dotenv


class Settings:
    load_dotenv()

    APP_NAME = os.environ.get("APP_NAME")


env_config = Settings

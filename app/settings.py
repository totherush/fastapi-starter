"""APP SETTINGS CONFIG"""
import os
from pydantic import BaseSettings


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", None)


class CommonSettings(BaseSettings):
    APP_NAME: str = "blogpost api"
    DEBUG_MODE: bool = bool(os.getenv("DEBUG"))


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_NAME: str = os.getenv("MONGODB_NAME", "")
    DB_URI: str = os.getenv("MONGODB_URI", "")


class SlackSettings(BaseSettings):
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
    SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "xyz")


class Settings(
    CommonSettings,
    DatabaseSettings,
    EnvironmentSettings,
    ServerSettings,
    SlackSettings,
):
    pass


settings = Settings()

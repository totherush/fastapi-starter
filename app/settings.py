"""APP SETTINGS CONFIG"""
import os
from pydantic import BaseSettings


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", None)


class CommonSettings(BaseSettings):
    APP_NAME: str = "payment service"
    DEBUG_MODE: bool = bool(os.getenv("DEBUG"))


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = os.getenv("MONGODB_URL", "")


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

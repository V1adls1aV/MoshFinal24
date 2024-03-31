from functools import lru_cache
from pydantic_settings import BaseSettings
from os import environ as env
import logging


class Settings(BaseSettings):
    LOG_LEVEL: int = logging.DEBUG

    POSTGRES_USER: str = env.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = env.get('POSTGRES_PASSWORD')
    POSTGRES_PORT: str = env.get('POSTGRES_PORT')
    POSTGRES_HOST: str = env.get('POSTGRES_HOST')
    POSTGRES_DB: str = env.get('POSTGRES_DB')

    POSTGRES_URL: str = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}' \
        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    

@lru_cache()
def get_app_settings() -> Settings:
    return Settings()

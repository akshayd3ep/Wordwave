from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field



class Settings(BaseSettings):
    ENVIRONMENT : str = "local"
    DATABASE_URL: str
    REDIS_URL: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DEBUG: bool = True



@lru_cache
def get_settings() -> Settings:
    return Settings()
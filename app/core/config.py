from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2] 

class Settings(BaseSettings):
    database_url: str
    async_database_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int
    project_name: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
print("[DEV]","Loaded settings:", settings)
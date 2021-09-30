import secrets
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_PATH: str = "/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_HOST: AnyHttpUrl
    PROJECT_NAME: str
    POSTGRESQL_DATABASE_URI: PostgresDsn

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

TORTOISE_CONFIG = {
    "connections": {"default": settings.POSTGRESQL_DATABASE_URI},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

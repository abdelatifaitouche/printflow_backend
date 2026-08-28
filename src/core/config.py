from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    JWT_SECRET_KEY: str
    JWT_ALGO: str
    ACCESS_TOKEN_DURATION: int
    REFRESH_TOKEN_DURATION: int

    model_config = {
        "env_file": ".env",
    }


settings = Settings()

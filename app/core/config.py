from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Secure REST API"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/secure_rest_api"
    jwt_secret: str = "change-me"

    class Config:
        env_file = ".env"


settings = Settings()

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "FastAPI Audio Service"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Яндекс OAuth
    YANDEX_CLIENT_ID: str = os.getenv("YANDEX_CLIENT_ID")
    YANDEX_CLIENT_SECRET: str = os.getenv("YANDEX_CLIENT_SECRET")
    YANDEX_REDIRECT_URI: str = os.getenv("YANDEX_REDIRECT_URI")

    # JWT токены
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"


settings = Settings()

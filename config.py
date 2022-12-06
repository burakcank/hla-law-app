"""Configuration classes."""
from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.absolute() / ".env")


class Config:
    """Base config."""

    SESSION_TYPE = "filesystem"

    # If this key is not set, then google maps will show as image under contact page.
    GOOGLE_MAPS_API_KEY = environ.get("GOOGLE_MAPS_API_KEY")

    # Unsplash access key
    UNSPLASH_ACCESS_KEY = environ.get("UNSPLASH_ACCESS_KEY")

    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = int(environ.get("MAIL_PORT"))
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USE_SSL = environ.get("MAIL_USE_SSL", True)
    MAIL_USE_TLS = environ.get("MAIL_USE_TLS", False)
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")

    LANGUAGES = {
        "en": "English",
        "tr": "Turkish",
    }


class ProdConfig(Config):
    SECRET_KEY = environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = environ["SQLALCHEMY_DATABASE_URI"]


class DevConfig(Config):
    SECRET_KEY = environ.get("SECRET_KEY", "some_very_secret_key")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI", "db.sqlite")

"""Configuration file."""
import pathlib
from os import environ

from dotenv import load_dotenv

basedir = pathlib.Path(__file__).parent.absolute()
load_dotenv(basedir / ".env")


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_TYPE = "filesystem"
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    PASSWORD_HASH_ROUNDS = int(environ.get("PASSWORD_HASH_ROUNDS", 10))
    GOOGLE_MAPS_API_KEY = environ.get("GOOGLE_MAPS_API_KEY")

    LANGUAGES = {
        "en": "English",
        "tr": "Turkish",
    }


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEV_DATABASE_URI")
    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = int(environ.get("MAIL_PORT"))
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_USE_SSL = environ.get("MAIL_USE_SSL")
    MAIL_USE_TLS = environ.get("MAIL_USE_TLS")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")
    USE_CREDENTIALS = True

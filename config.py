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

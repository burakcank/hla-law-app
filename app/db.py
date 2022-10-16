from sqlalchemy import create_engine

from app.models import Base

engine = create_engine("sqlite:///sqlite.db")


def init_db():
    Base.metadata.create_all(engine)

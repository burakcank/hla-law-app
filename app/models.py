from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class EmailRequest(Base):
    __tablename__ = "email_requests"

    id = Column(Integer, primary_key=True)
    sent_to = Column(String)
    sent_from = Column(String)
    content = Column(String)

    def __repr__(self) -> str:
        return f"EmailRequest <{self.id}>"

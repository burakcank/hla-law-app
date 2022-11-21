from sqlalchemy import Column, Integer, String

from app import db


class EmailRequest(db.Model):
    __tablename__ = "email_requests"

    id = Column(Integer, primary_key=True)
    sent_to = Column(String, nullable=False)
    sent_from = Column(String, nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<EmailRequest {self.id}>"

from sqlalchemy import (
    Column,
    Integer, String,
    func, DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String, unique=True)
    answer = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True))

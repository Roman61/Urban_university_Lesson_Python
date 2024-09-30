from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from user import User

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, default=0)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    slug = relationship("User", back_populates="tasks")

    products = relationship("Product", back_populates="category")


print(CreateTable(Task.__table__))

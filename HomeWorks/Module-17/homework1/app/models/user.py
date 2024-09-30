import sys
sys.path.append('D:\LessonPy\Urban_university_Lesson_Python\HomeWorks\Module-17\homework1\app')
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from task import Task

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, default=0)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Product", back_populates="category")
    # - объект связи с таблицей с таблицей Task, где back_populates = 'user'.


print(CreateTable(User.__table__))

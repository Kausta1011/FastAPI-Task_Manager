from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String 
from database import Base

class Tasks(Base):

    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key = True, index = True)
    task_title = Column(String)
    task_description = Column(String)
    task_priority = Column(String)
    task_status = Column(String)



# calculator_app/database/models.py
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Calculation(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    result = Column(Float, nullable=False)

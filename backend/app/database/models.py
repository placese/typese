from sqlalchemy import Column, Integer, String, Boolean, Date, Time, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    """ORM class of user model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean)

    base_test_results = relationship('BaseTestResult')


class BaseTestResult(Base):
    """ORM class of base test result"""
    __tablename__ = 'base_test_results'

    id = Column(Integer, primary_key=True, index=True)
    pass_date = Column(Date)
    pass_time = Column(Time)
    wpm = Column(Integer)
    spm = Column(Integer)
    accuracy = Column(Float)

    user_id = Column(Integer, ForeignKey('users.id'))

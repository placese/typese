from pydantic import BaseModel
from datetime import date, time


class BaseTestResultBase(BaseModel):
    """Pydantic base model of base test result"""
    pass_date: date
    pass_time: time
    wpm: int
    spm: int
    accuracy: float


class BaseTestResultCreate(BaseTestResultBase):
    """Pydantic model to create BaseTestResult"""
    pass


class BaseTestResult(BaseTestResultBase):
    """"Pydantic model to get Test Result"""
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    """Pydantic base model of user"""
    user_name: str
    email: str


class UserCreate(UserBase):
    """Pydantic model to create user"""
    password: str


class User(UserBase):
    """Pydantic model to get user"""
    id: int
    # hashed_password: str
    is_active: bool
    base_test_results: list[BaseTestResult] | None = None

    class Config:
        orm_mode = True

from sqlalchemy.orm import Session
from app.auth.password_handler import hash_password
from . import models, schemas


def get_user(db: Session, user_id: int) -> schemas.User:
    """Returns user from db by it's id"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str) -> schemas.User | None:
    """Returns user from db by email"""
    return db.query(models.User).filter(models.User.email == user_email).first()

def get_user_by_user_name(db: Session, user_name: str) -> schemas.User | None:
    """Returns user from db by user name"""
    return db.query(models.User).filter(models.User.user_name == user_name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.User]:
    """Return list of users with offset and limit"""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User | None:
    """Creates user in db and returns it if user is not exist, in other case returns None"""
    hashed_password = hash_password(user.password)
    db_user = models.User(user_name=user.user_name, email=user.email, hashed_password=hashed_password, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_base_test_result(db: Session, test_id: int) -> schemas.BaseTestResult:
    """Returns base test result by it's id"""
    return db.query(models.BaseTestResult).filter(models.BaseTestResult.id == test_id).first()


def get_base_test_results(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.BaseTestResult]:
    """Returns list of base test results with offset and limit"""
    return db.query(models.BaseTestResult).offset(skip).limit(limit).all()


def get_base_test_results_by_user_id(db: Session, user_id, skip: int = 0, limit: int = 100) -> list[schemas.BaseTestResult]:
    """Returns list of base test results of currend user by user's id with offset and limit"""
    return db.query(models.BaseTestResult).filter(models.BaseTestResult.user_id == user_id).offset(skip).limit(limit).all()


def create_base_test_result(db: Session, base_test_result: schemas.BaseTestResultCreate, user_id: int) -> schemas.BaseTestResult:
    """Creates base test result in db and returns it"""
    db_base_test_result = models.BaseTestResult(**base_test_result.dict(), user_id=user_id)
    db.add(db_base_test_result)
    db.commit()
    db.refresh(db_base_test_result)
    return db_base_test_result

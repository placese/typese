from passlib.context import CryptContext
from app.database import schemas
import app.database.crud as crud


pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def varify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def check_user_in_db(user: schemas.User) -> bool:
    """Returns True if user exists in db"""
    return crud.get_user(user.id) is not None


def get_hashed_user_password(user: schemas.User) -> str:
    """Returns hashed user's password"""
    return crud.get_user(user.id).hashed_password


def hash_password(plain_password: str) -> str:
    """Returns hashed password with salt"""
    return pwd_context.hash(plain_password)


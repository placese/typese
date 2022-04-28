
import time
from jose import jwt


JWT_SECRET_KEY = '359ff32f33b76184b482a426e12be7d07e6249d369e4846b205fa881d34123e5'
JWT_ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRES_MINUTES = 600


def token_response(token: str):
    """Returns the generated JWT tokens"""
    return {
        "access token": token
    }


def sign_JWT(user_id: str):
    """Sings the JWT string"""
    payload = {
        'user_id': user_id,
        'expiry': time.time() + ACCESS_TOKEN_EXPIRES_MINUTES
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_JWT(token: str):
    """Returns the decoded jwt token if it didn't expires, it other case returns None"""
    try:
        decode_token = jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return {}
from datetime import datetime, timedelta, timezone

import aiohttp
import jwt
from databases import Database
from passlib.context import CryptContext

SECRET_KEY = 'your_secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
database = Database('sqlite:///example.db')


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    query = (
        "SELECT hashed_password FROM users WHERE plain_password = :plain_password"
    )
    result = await database.fetch_one(
        query=query, values={"plain_password": plain_password}
    )
    if result:
        return pwd_context.verify(plain_password, result['hashed_password'])
    return False


async def create_access_token(
    data: dict, expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

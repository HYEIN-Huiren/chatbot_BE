import os
from core.config import getConfig

from passlib.context import CryptContext

import redis

from auth.repo import loadUserByUserId
from jose import jwt
from datetime import datetime, timedelta, timezone

config = getConfig()

# rd=redis.StrictRedis(host=config.get('REDIS_HOST'), port=config.get('REDIS_PORT'))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, userId: str, password: str):
    user = loadUserByUserId(db, userId)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes= 30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.get('SECRET_KEY'), algorithm=config.get('ALGORITHM'))
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days= 1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.get('SECRET_KEY'), algorithm=config.get('ALGORITHM'))
    
    # rd.set(data.get('userId'), encoded_jwt)

    return encoded_jwt
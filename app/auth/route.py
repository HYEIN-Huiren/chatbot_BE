import os
from core.config import getConfig

from core.bearer import JWTBearer
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.connection import get_db
from auth.models.dto import LoginRequest, Token
from auth.repo import loadUserByUserId, getMenuList
from auth.impl import create_access_token, create_refresh_token, verify_password
from jose import jwt
import redis
from datetime import datetime, timezone

auth = APIRouter(
    prefix="/auth", # url 앞에 고정적으로 붙는 경로추가
    tags=['Auth'],
) # Route 분리

config = getConfig()

rd=redis.StrictRedis(host=config.get('REDIS_HOST'), port=config.get('REDIS_PORT'))

@auth.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = loadUserByUserId(db, request.userId)
    if user:
        if verify_password(request.password, user.password):
            accessToken = create_access_token({"userId": user.userId,
                                               "timeZoneID": "GMT+00:00",
                                               "language": user.language
                                               })
            refreshToken = create_refresh_token({"userId": user.userId})
            menuList=getMenuList(db, request.userId)

            return {
                "message": None,
                "data": {
                    "accessToken": accessToken,
                    "refreshToken": refreshToken,
                    "userInfo": user,
                    "menuList":menuList,
                },
                "pageInfo": None,
                "isSuccess": True
                }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail = "Incorrect password",
                headers={"WWW-Authenticate": "Bearer"}
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect userId",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
@auth.post("/refresh-token"
        #    , dependencies=[Depends(JWTBearer())]
           )
async def login_for_refresh_token(request: Token, db: Session = Depends(get_db)):
    # try:
        payload = jwt.decode(request.refreshToken, config.get('SECRET_KEY'), algorithms=config.get('ALGORITHM'))
        userId=payload.get('userId')
        user = loadUserByUserId(db, userId)
        if user:
            # if rd.get("userId") == request.refreshToken:
            if payload.get('exp') < int(datetime.now(timezone.utc).timestamp()):
                    raise HTTPException(
                    status_code=5007, #JWT_REFRESH_TOKEN_EXPIRED
                    detail= "Jwt Token Expired",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            else:
                    accessToken = create_access_token({"userId": user.userId,
                                                "timeZoneID": "GMT+00:00",
                                                "language": user.language
                                                })
                    # refreshToken = create_refresh_token({'userId': userId})
                    return {
                        "message": None,
                        "data": {
                            "accessToken": accessToken
                        },
                        "pageInfo": None,
                        "isSuccess": True
                        }
            # else:
            #     return {"msg": 'redis error'}
        else:
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail = "No such user",
                    headers={"WWW-Authenticate": "Bearer"}
            )
    # except:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail = "Not valid refresh token",
    #         headers={"WWW-Authenticate": "Bearer"}
    #     )

@auth.post("/logout", dependencies=[Depends(JWTBearer())],)
async def logout(token: str = Depends(JWTBearer()), db: Session = Depends(get_db)):
    try:
        user = jwt.decode(token, config.get('SECRET_KEY'), algorithms=config.get('ALGORITHM'))
        # rd.delete(user.get('userId'))

        return {
                    "message": 'Logout success',
                    "data": None,
                    "pageInfo": None,
                    "isSuccess": True
                    }
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Not valid refresh token",
            headers={"WWW-Authenticate": "Bearer"}
        )

# from datetime import datetime, timedelta
from jose import  jwt
from typing import Dict
import time
from .. import config

secret_key =  config.SECRET_KEY
algorithm = config.ALGORITHM
access_token_expire_minutes = int(config.ACCESS_TOKEN_EXPIRE_MINUTES)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = time.time() + access_token_expire_minutes
    to_encode.update({"expires": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
        # return decoded_token if decoded_token["expires"] >= time.time() else None
        return decoded_token
    except:
        return {}
    
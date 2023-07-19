from pydantic import BaseModel,Field
from fastapi import Form

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class TokenResponse(BaseModel):
    access_token: str=Field("")
    token_type: str=Field("")

class Login(BaseModel):
    username:str=Form(...)
    password:str=Form(...)

class User(BaseModel):
    name:str
    email:str
    password:str
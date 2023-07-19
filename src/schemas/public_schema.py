from pydantic import BaseModel,EmailStr, Field, validator
from datetime import datetime

class GetTenants(BaseModel):
    Name:str=Field("")
    Email:str=Field("")
    Created_at:datetime=Field("")
    class Config():
        orm_mode = True

class PostTenant(BaseModel):
    Name: str = Field(...)
    Email: str = Field(...)
    Password: str = Field(...)
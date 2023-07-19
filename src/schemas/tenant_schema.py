from pydantic import BaseModel,EmailStr, Field, validator
from datetime import datetime


class AddData(BaseModel):
    Title:str=''
    Desc:str=''
    class Config:
        orm_mode = True

class GetData(BaseModel):
    Title:str=''
    Desc:str=''
    class Config:
        orm_mode = True

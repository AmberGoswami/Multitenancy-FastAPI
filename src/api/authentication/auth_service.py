from sqlalchemy.orm import Session
from ...models import models
from fastapi import HTTPException,status,Request
from ...helpers.hashing import *
from...helpers import token

def login(username,password, db:Session):
    user = db.query(models.Tenants).filter(
    models.Tenants.Email == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.Password,password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    access_token = token.create_access_token(data={"id":str(user.Id),"name":user.Name,"email":user.Email})
    return {"access_token": access_token, "token_type": "bearer"}

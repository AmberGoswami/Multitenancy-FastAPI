from urllib.parse import urlparse
from fastapi import Request, status,HTTPException,UploadFile
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from ...models import models
import pathlib,uuid
from ...helpers import token

def add_data(request,title,desc,db:Session):
    bearer = request.headers.get("Authorization").split()[1]
    data=token.decodeJWT(bearer)
    tenant= data.get('name')
    table = getattr(models, f"Table_{tenant}")
    try:
        data = table(Title=title, Desc=desc)
        db.add(data)
        db.commit()
        return {"detail":"data added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_data(request,db:Session):
    bearer = request.headers.get("Authorization").split()[1]
    data=token.decodeJWT(bearer)
    tenant= data.get('name')
    table = getattr(models, f"Table_{tenant}")
    try:
        data=db.query(table).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

def delete_data(request,db:Session):
    bearer = request.headers.get("Authorization").split()[1]
    data=token.decodeJWT(bearer)
    tenant= data.get('name')
    table = getattr(models, f"Table_{tenant}")    
    try:
        db.query(table).delete(synchronize_session=False)
        db.commit()
        return {"detail":"Data Deleted"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


    
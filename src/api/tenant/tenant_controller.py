from typing import List
from urllib.parse import urlparse
from fastapi import APIRouter,Depends, Form,Path, Query,status,File, UploadFile,Response,Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from ...db.db import *
from sqlalchemy.orm import Session
from .tenant_service import *
from ...schemas import tenant_schema,auth_schema
from ...helpers import bearer
security = HTTPBearer()

router = APIRouter(   
    tags=['Tenant-Based-Main'],
    prefix='/v1'
)


@router.post("/add-data",dependencies=[Depends(bearer.JWTBearer())],status_code=status.HTTP_202_ACCEPTED)
async def ADD_DATA(request:Request,payload:tenant_schema.AddData,db: Session = Depends(get_public_db)):
    '''
    Add data in the tenant specific table
    '''
    return add_data(request,payload.Title,payload.Desc,db)

@router.get("/get-data",dependencies=[Depends(bearer.JWTBearer())],status_code=status.HTTP_200_OK,response_model=list[tenant_schema.GetData])
async def GET_DATA(request:Request,db: Session = Depends(get_public_db)):
    '''
    Get data from the tenant specific table
    '''
    return get_data(request,db)


@router.delete("/delete-all",dependencies=[Depends(bearer.JWTBearer())],status_code=status.HTTP_200_OK)
async def DELETE_DATA(request:Request,db: Session = Depends(get_public_db)):
    '''
    Delete data from the tenant specific table
    '''
    return delete_data(request,db)




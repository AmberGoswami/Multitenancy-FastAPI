from typing import List
from fastapi import APIRouter,Depends,Path,status
from ...db.db import*
from sqlalchemy.orm import Session
from .public_service import *
from ...schemas import public_schema
from ...helpers import bearer

router = APIRouter(   
    tags=['Public-Based'],
    prefix='/v1'
)

@router.post('/add-tenant',status_code=status.HTTP_201_CREATED)
async def ADD_TENANT(request: public_schema.PostTenant, db:Session=Depends(get_public_db)):
    '''
    Add tenants
    '''
    return add_tenant(request.Name,request.Email,request.Password,db)

@router.get('/get-tenants',response_model=List[public_schema.GetTenants],status_code=status.HTTP_202_ACCEPTED)
async def GET_TENANTS(db:Session=Depends(get_public_db)):
    '''
    Get tenants 
    '''
    return get_tenants(db)
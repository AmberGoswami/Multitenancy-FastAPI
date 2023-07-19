from fastapi import APIRouter,Depends, Form,Request
from sqlalchemy.orm import Session
from ...db.db import *
from .auth_service import *
from ...schemas import auth_schema

router=APIRouter(tags=['Authentication'],
                 prefix='/v1')

@router.post('/sign-in',response_model=auth_schema.TokenResponse)
def SIGN_IN(payload:auth_schema.Login,db:Session=Depends(get_public_db)):
    '''
    Tenant Login
    '''
    return login(payload.username,payload.password,db)

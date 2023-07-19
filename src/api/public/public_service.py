from sqlalchemy import text
from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from ...models import models
from...helpers import migrations,hashing

def add_tenant(schema_name:str, email:str, password:str, db:Session):
    try:
        Text = text(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
        db.execute(Text)
        db.commit()
        models.create_dynamic_classes()
        migrations.migrations()
        existing=db.query(models.Tenants).filter(models.Tenants.Email==email).first()
        if existing:
            res={"msg":"Tenant already exist"}
            return res
        if not existing:
            schema=models.Tenants(Name=schema_name,Email=email,Password=hashing.Hash.bcrypt(password))
            db.add(schema)
            db.commit()
            db.refresh(schema)            
            res={"msg":"Tenant Created"}
            return res           
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
def get_tenants(db:Session):
    try:
        data=db.query(models.Tenants).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=500)
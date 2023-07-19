from sqlalchemy import Boolean, Column, ForeignKey,Double, Integer, String,DateTime,func,inspect
from sqlalchemy.orm import relationship
from ..db.db import*
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Tenants(Base):
    __tablename__ = "tenants"
    __table_args__ = {"schema": "public"}
    Id=Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    Name=Column(String)
    Email=Column(String)
    Password=Column(String)
    Created_at=Column(DateTime,default=func.now())

def create_dynamic_classes():
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()
    visible_schemas = [schema for schema in schemas if not schema.startswith('pg_') and schema != 'information_schema' and schema != 'public']
    for schema in visible_schemas:
        class_name = f"Table_{schema}"
        if class_name not in globals():
            globals()[class_name] = type(
                class_name,
                (Base,),
                {
                    "__tablename__": "table",
                    "__table_args__": {"schema": schema},
                    "Id": Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                    "Title": Column(String),
                    "Desc": Column(String)
                },
            )
        
create_dynamic_classes()
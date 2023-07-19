from fastapi import Path,Request,HTTPException
from urllib.parse import urlparse
from sqlalchemy import create_engine,text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .. import config

database_url = config.DATABASE_URL

engine = create_engine(database_url)

def get_public_db():
    engine_public=create_engine(database_url)
    SessionLocal_public=sessionmaker(autocommit=False, autoflush=False, bind=engine_public)
    db=SessionLocal_public()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import Config.db, Models.model_rols, Schemas.schema_rol, Crud.crud_rol
from typing import List

rol=APIRouter()

Models.model_rols.Base.metadata.create_all(bind=Config.db.engine)

def get_db():
    db = Config.db.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@rol.get("/rol/", response_model=List[Schemas.schema_rol.RolResponse], tags=["Rols"])
async def read_rols(skip:int=0, limit: int = 10, db: Session = Depends(get_db)):
    db_rol = crud.crud_rol.get_rol(db=db, skip=skip, limit=limit)
    return db_rol
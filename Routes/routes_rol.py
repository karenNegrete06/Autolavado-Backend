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
    db_rol = Crud.crud_rol.get_rol(db=db, skip=skip, limit=limit)
    return db_rol

@rol.post("/rol/", response_model=Schemas.schema_rol.RolResponse, tags=["Rols"])
async def create_rol(rol: Schemas.schema_rol.RolCreate, db: Session = Depends(get_db)):
    db_rol = Crud.crud_rol.create_rol(db=db, rol=rol)
    return db_rol       

@rol.get("/rol/{rol_id}", response_model=Schemas.schema_rol.RolResponse, tags=["Rols"])
async def read_rol(rol_id: int, db: Session = Depends(get_db)): 
    db_rol = Crud.crud_rol.get_rol_by_id(db=db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol   

@rol.put("/rol/{rol_id}", response_model=Schemas.schema_rol.RolResponse, tags=["Rols"])
async def update_rol(rol_id: int, rol: Schemas.schema_rol.RolCreate, db: Session = Depends(get_db)):
    db_rol = Crud.crud_rol.update_rol(db=db, rol_id=rol_id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol

@rol.delete("/rol/{rol_id}", tags=["Rols"])
async def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    db_rol = Crud.crud_rol.delete_rol(db=db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"detail": "Rol eliminado exitosamente"} 





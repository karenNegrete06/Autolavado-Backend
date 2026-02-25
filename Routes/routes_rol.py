from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Config.security import get_current_user
import Config.db, Models.model_rols, Schemas.schema_rol, Crud.crud_rol
from typing import List

rol=APIRouter()



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
def create_rol(rol: Schemas.schema_rol.RolCreate, db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)):
    db_rol = Crud.crud_rol.get_rol_by_nombre(db, nombre_rol=rol.nombre_rol)
    if db_rol:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return Crud.crud_rol.create_rol(db=db, rol=rol)
  

@rol.put("/rol/{rol_id}", response_model=Schemas.schema_rol.RolResponse, tags=["Rols"])
async def update_rol(id: int, rol: Schemas.schema_rol.RolUpdate, db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)):
    db_rol = Crud.crud_rol.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no actualizado")
    return db_rol

@rol.delete("/rol/{rol_id}", tags=["Rols"])
async def delete_rol(id: int, db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)):
    db_rol = Crud.crud_rol.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El Rol no existe, no se pudo eliminar")
    return db_rol




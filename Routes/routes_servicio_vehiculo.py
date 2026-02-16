from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import Config.db, Models.model_servicio_vehiculo, Schemas.schema_servicio_vehiculo, Crud.crud_servicio_vehiculo
from typing import List

servicio_vehiculo=APIRouter()

def get_db():
    db = Config.db.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
@servicio_vehiculo.get("/servicio_vehiculo/", response_model=List[Schemas.schema_servicio_vehiculo.ServicioVehiculoResponse], tags=["Servicio_Vehiculo"])
async def read_servicio_vehiculo(skip:int=0, limit: int = 10, db: Session = Depends(get_db)):
    db_servicio_vehiculo = Crud.crud_servicio_vehiculo.get_servicio_vehiculo(db=db, skip=skip, limit=limit)
    return db_servicio_vehiculo

@servicio_vehiculo.post("/servicio_vehiculo/", response_model=Schemas.schema_servicio_vehiculo.ServicioVehiculoResponse, tags=["Servicio_Vehiculo"])
async def create_servicio_vehiculo(servicio_vehiculo: Schemas.schema_servicio_vehiculo.ServicioVehiculoCreate, db: Session = Depends(get_db)):
    db_servicio_vehiculo = Crud.crud_servicio_vehiculo.create_servicio_vehiculo(db=db, servicio_vehiculo=servicio_vehiculo)
    return db_servicio_vehiculo

@servicio_vehiculo.get("/servicio_vehiculo/{as_id}", response_model=Schemas.schema_servicio_vehiculo.ServicioVehiculoResponse, tags=["Servicio_Vehiculo"])
async def read_servicio_vehiculo(as_id: int, db: Session = Depends(get_db)): 
    db_servicio_vehiculo = Crud.crud_servicio_vehiculo.get_servicio_vehiculo_by_id(db=db, as_id=as_id)
    if db_servicio_vehiculo is None:
        raise HTTPException(status_code=404, detail="Servicio_Vehiculo no encontrado")
    return db_servicio_vehiculo

@servicio_vehiculo.put("/servicio_vehiculo/{as_id}", response_model=Schemas.schema_servicio_vehiculo.ServicioVehiculoResponse, tags=["Servicio_Vehiculo"])
async def update_servicio_vehiculo(as_id: int, servicio_vehiculo: Schemas.schema_servicio_vehiculo.ServicioVehiculoCreate, db: Session = Depends(get_db)):
    db_servicio_vehiculo = Crud.crud_servicio_vehiculo.update_servicio_vehiculo(db=db, as_id=as_id, servicio_vehiculo=servicio_vehiculo)
    if db_servicio_vehiculo is None:
        raise HTTPException(status_code=404, detail="Servicio_Vehiculo no encontrado")
    return db_servicio_vehiculo 

@servicio_vehiculo.delete("/servicio_vehiculo/{as_id}", tags=["Servicio_Vehiculo"])
async def delete_servicio_vehiculo(as_id: int, db: Session = Depends(get_db)):
    db_servicio_vehiculo = Crud.crud_servicio_vehiculo.delete_servicio_vehiculo(db=db, as_id=as_id)
    if db_servicio_vehiculo is None:
        raise HTTPException(status_code=404, detail="Servicio_Vehiculo no encontrado")
    return {"detail": "Servicio_Vehiculo eliminado exitosamente"}


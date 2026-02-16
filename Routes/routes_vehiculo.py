from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import Config.db, Models.model_vehiculo, Schemas.schema_vehiculo, Crud.crud_vehiculo
from typing import List

vehiculo=APIRouter()

def get_db():
    db = Config.db.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@vehiculo.get("/vehiculo/", response_model=List[Schemas.schema_vehiculo.VehiculoResponse], tags=["Vehiculo"])
async def read_vehiculos(skip:int=0, limit: int = 10, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.get_vehiculo(db=db, skip=skip, limit=limit)
    return db_vehiculo

@vehiculo.post("/vehiculo/", response_model=Schemas.schema_vehiculo.VehiculoResponse, tags=["Vehiculo"])
async def create_vehiculo(vehiculo: Schemas.schema_vehiculo.VehiculoCreate, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.create_vehiculo(db=db, vehiculo=vehiculo)
    return db_vehiculo

@vehiculo.get("/vehiculo/{ve_id}", response_model=Schemas.schema_vehiculo.VehiculoResponse, tags=["Vehiculo"])
async def read_vehiculo(ve_id: int, db: Session = Depends(get_db)): 
    db_vehiculo = Crud.crud_vehiculo.get_vehiculo_by_id(db=db, ve_id=ve_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return db_vehiculo

@vehiculo.put("/vehiculo/{ve_id}", response_model=Schemas.schema_vehiculo.VehiculoResponse, tags=["Vehiculo"])
async def update_vehiculo(ve_id: int, vehiculo: Schemas.schema_vehiculo.VehiculoCreate, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.update_vehiculo(db=db, ve_id=ve_id, vehiculo=vehiculo)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return db_vehiculo

@vehiculo.delete("/vehiculo/{ve_id}", tags=["Vehiculo"])
async def delete_vehiculo(ve_id: int, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.delete_vehiculo(db=db, ve_id=ve_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return {"detail": "Vehiculo eliminado exitosamente"}

@vehiculo.get("/vehiculo/placa/{ve_placa}", response_model=Schemas.schema_vehiculo.VehiculoResponse, tags=["Vehiculo"])
async def read_vehiculo_by_placa(ve_placa: str, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.get_vehiculo_by_placa(db=db, ve_placa=ve_placa)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return db_vehiculo


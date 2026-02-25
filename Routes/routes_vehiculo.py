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
def create_vehiculo(vehiculo: Schemas.schema_vehiculo.VehiculoCreate, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.get_vehiculo_by_nombre(db, placas=vehiculo.placas)
    if db_vehiculo:
        raise HTTPException(status_code=400, detail="Vehiculo existente intenta nuevamente")
    return Crud.crud_vehiculo.create_vehiculo(db=db, vehiculo=vehiculo)


@vehiculo.put("/vehiculo/{ve_id}", response_model=Schemas.schema_vehiculo.VehiculoResponse, tags=["Vehiculo"])
async def update_vehiculo(id: int, vehiculo: Schemas.schema_vehiculo.VehiculoUpdate, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.update_vehiculo(db=db, id=id, vehiculo=vehiculo)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculos no existe, no actualizado")
    return db_vehiculo

@vehiculo.delete("/vehiculo/{ve_id}", tags=["Vehiculo"])
async def delete_vehiculo(id: int, db: Session = Depends(get_db)):
    db_vehiculo = Crud.crud_vehiculo.delete_vehiculo(db=db, id=id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="El vehiculo no existe, no se pudo eliminar")
    return db_vehiculo




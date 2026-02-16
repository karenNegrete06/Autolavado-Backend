from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import Config.db, Models.model_servicio, Schemas.schema_servicio, Crud.crud_servicio
from typing import List

servicio=APIRouter()
Models.model_servicio.Base.metadata.create_all(bind=Config.db.engine)

def get_db():
    db = Config.db.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@servicio.get("/servicio/", response_model=List[Schemas.schema_servicio.ServicioResponse], tags=["Servicio"])
async def read_servicios(skip:int=0, limit: int = 10, db: Session = Depends(get_db)):
    db_servicio = Crud.crud_servicio.get_servicio(db=db, skip=skip, limit=limit)
    return db_servicio

@servicio.post("/servicio/", response_model=Schemas.schema_servicio.ServicioResponse, tags=["Servicio"])
async def create_servicio(servicio: Schemas.schema_servicio.ServicioCreate, db: Session = Depends(get_db)):
    db_servicio = Crud.crud_servicio.create_servicio(db=db, servicio=servicio)
    return db_servicio

@servicio.get("/servicio/{se_id}", response_model=Schemas.schema_servicio.ServicioResponse, tags=["Servicio"])
async def read_servicio(se_id: int, db: Session = Depends(get_db)): 
    db_servicio = Crud.crud_servicio.get_servicio_by_id(db=db, se_id=se_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicio.put("/servicio/{se_id}", response_model=Schemas.schema_servicio.ServicioResponse, tags=["Servicio"])
async def update_servicio(se_id: int, servicio: Schemas.schema_servicio.ServicioCreate, db: Session = Depends(get_db)):
    db_servicio = Crud.crud_servicio.update_servicio(db=db, se_id=se_id, servicio=servicio)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio  

@servicio.delete("/servicio/{se_id}", tags=["Servicio"])
async def delete_servicio(se_id: int, db: Session = Depends(get_db)):
    db_servicio = Crud.crud_servicio.delete_servicio(db=db, se_id=se_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"detail": "Servicio eliminado exitosamente"}

@servicio.get("/servicio/nombre/{se_nombre}", response_model=Schemas.schema_servicio.ServicioResponse, tags=["Servicio"])
async def read_servicio_by_nombre(se_nombre: str, db: Session = Depends(get_db)):
    db_servicio = Crud.crud_servicio.get_servicio_by_nombre(db=db, se_nombre=se_nombre)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio


import Models.model_servicio_vehiculo
import Schemas.schema_servicio_vehiculo
from sqlalchemy.orm import Session
def get_servicio_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).offset(skip).limit(limit).all()

def get_servicio_vehiculo_by_id(db: Session, as_id: int):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.as_id == as_id).first()

def create_servicio_vehiculo(db: Session, servicio_vehiculo: Schemas.schema_servicio_vehiculo.ServicioVehiculoCreate):
    db_servicio_vehiculo = Models.model_servicio_vehiculo.ServicioVehiculo(
        au_id=servicio_vehiculo.au_id,
        cajero_id=servicio_vehiculo.cajero_id,
        operativo_id=servicio_vehiculo.operativo_id,
        se_id=servicio_vehiculo.se_id,
        as_fecha=servicio_vehiculo.as_fecha,
        as_hora=servicio_vehiculo.as_hora,
        as_estatus=servicio_vehiculo.as_estatus,
        as_estado=servicio_vehiculo.as_estado,
        fecha_registro=servicio_vehiculo.fecha_registro,
        fecha_modificacion=servicio_vehiculo.fecha_modificacion
    )
    db.add(db_servicio_vehiculo)
    db.commit()
    db.refresh(db_servicio_vehiculo)
    return db_servicio_vehiculo

def update_servicio_vehiculo(db: Session, as_id: int, servicio_vehiculo: Schemas.schema_servicio_vehiculo.ServicioVehiculoCreate):
    db_servicio_vehiculo = db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.as_id == as_id).first()
    if db_servicio_vehiculo is None:
        return None
    db_servicio_vehiculo.au_id = servicio_vehiculo.au_id
    db_servicio_vehiculo.cajero_id = servicio_vehiculo.cajero_id
    db_servicio_vehiculo.operativo_id = servicio_vehiculo.operativo_id
    db_servicio_vehiculo.se_id = servicio_vehiculo.se_id
    db_servicio_vehiculo.as_fecha = servicio_vehiculo.as_fecha
    db_servicio_vehiculo.as_hora = servicio_vehiculo.as_hora
    db_servicio_vehiculo.as_estatus = servicio_vehiculo.as_estatus
    db_servicio_vehiculo.as_estado = servicio_vehiculo.as_estado
    db_servicio_vehiculo.fecha_modificacion = servicio_vehiculo.fecha_modificacion
    db.commit()
    db.refresh(db_servicio_vehiculo)
    return db_servicio_vehiculo

def delete_servicio_vehiculo(db: Session, as_id: int):
    db_servicio_vehiculo = db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.as_id == as_id).first()
    if db_servicio_vehiculo is None:
        return None
    db.delete(db_servicio_vehiculo)
    db.commit()
    return db_servicio_vehiculo

def get_servicio_vehiculo_by_au_id(db: Session, au_id: int):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.au_id == au_id).first()

def get_servicio_vehiculo_by_cajero_id(db: Session, cajero_id: int):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.cajero_id == cajero_id).first()

def get_servicio_vehiculo_by_operativo_id(db: Session, operativo_id: int):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.operativo_id == operativo_id).first()

def get_servicio_vehiculo_by_se_id(db: Session, se_id: int):
    return db.query(Models.model_servicio_vehiculo.ServicioVehiculo).filter(Models.model_servicio_vehiculo.ServicioVehiculo.se_id == se_id).first()


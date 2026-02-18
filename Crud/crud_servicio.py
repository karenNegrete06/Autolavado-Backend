
from Models.model_servicio import Servicio
import Schemas.schema_servicio
from sqlalchemy.orm import Session

def get_servicio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Servicio).offset(skip).limit(limit).all()

def get_servicio_by_id(db: Session, se_id: int):
    return db.query(Servicio).filter(Servicio.se_id == se_id).first()

def create_servicio(db: Session, servicio: Schemas.schema_servicio.ServicioCreate):
    db_servicio = Servicio(
        se_nombre=servicio.se_nombre,
        se_descripcion=servicio.se_descripcion,
        se_precio=servicio.se_precio,
        se_estatus=servicio.se_estatus,
        se_duracion_minutos=servicio.se_duracion_minutos,
        us_id=servicio.us_id,
        fecha_registro=servicio.fecha_registro,
        fecha_modificacion=servicio.fecha_modificacion
    )
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, se_id: int, servicio: Schemas.schema_servicio.ServicioCreate):
    db_servicio = db.query(Servicio).filter(Servicio.se_id == se_id).first()
    if db_servicio is None:
        return None
    db_servicio.se_nombre = servicio.se_nombre
    db_servicio.se_descripcion = servicio.se_descripcion
    db_servicio.se_estatus = servicio.se_estatus
    db_servicio.se_duracion_minutos = servicio.se_duracion_minutos
    db_servicio.fecha_modificacion = servicio.fecha_modificacion
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, se_id: int):
    db_servicio = db.query(Servicio).filter(Servicio.se_id == se_id).first()
    if db_servicio is None:
        return None
    db.delete(db_servicio)
    db.commit()
    return db_servicio

def get_servicio_by_nombre(db: Session, se_nombre: str):
    return db.query(Servicio).filter(Servicio.se_nombre == se_nombre).first()



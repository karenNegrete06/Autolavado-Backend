
from Models.model_rols import Rol

import Schemas.schema_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rol).offset(skip).limit(limit).all()

def get_rol_by_id(db: Session, rol_id: int):
    return db.query(Rol).filter(Rol.id == rol_id).first()

def create_rol(db: Session, rol: Schemas.schema_rol.RolCreate):
    db_rol = Rol(
        nombre=rol.nombre,
        estatus=rol.estatus,
        fecha_registro=rol.fecha_registro,
        fecha_modificacion=rol.fecha_modificacion
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: Schemas.schema_rol.RolCreate):
    db_rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if db_rol is None:
        return None
    db_rol.nombre = rol.nombre
    db_rol.estatus = rol.estatus 
    db_rol.fecha_modificacion = rol.fecha_modificacion
    db.commit()
    db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    db_rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if db_rol is None:
        return None
    db.delete(db_rol)
    db.commit()
    return db_rol

def get_rol_by_nombre(db: Session, nombre: str):
    return db.query(Rol).filter(Rol.nombre == nombre).first()


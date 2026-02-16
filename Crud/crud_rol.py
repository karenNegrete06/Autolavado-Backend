import Models.model_rols
import Schemas.schema_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.model_rols).offeset(skip).limit(limit).all()

def get_rol_by_id(db: Session, rol_id: int):
    return db.query(Models.model_rols).filter(Models.model_rols.rol_id == rol_id).first()

def create_rol(db: Session, rol: Schemas.schema_rol.RolCreate):
    db_rol = Models.model_rols(
        rol_nombre=rol.rol_nombre,
        rol_descripcion=rol.rol_descripcion,
        rol_estado=rol.rol_estado,
        fecha_registro=rol.fecha_registro,
        fecha_modificacion=rol.fecha_modificacion
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: Schemas.schema_rol.RolCreate):
    db_rol = db.query(Models.model_rols).filter(Models.model_rols.rol_id == rol_id).first()
    if db_rol is None:
        return None
    db_rol.rol_nombre = rol.rol_nombre
    db_rol.rol_descripcion = rol.rol_descripcion
    db_rol.rol_estado = rol.rol_estado
    db_rol.fecha_modificacion = rol.fecha_modificacion
    db.commit()
    db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    db_rol = db.query(Models.model_rols).filter(Models.model_rols.rol_id == rol_id).first()
    if db_rol is None:
        return None
    db.delete(db_rol)
    db.commit()
    return db_rol

def get_rol_by_nombre(db: Session, rol_nombre: str):
    return db.query(Models.model_rols).filter(Models.model_rols.rol_nombre == rol_nombre).first()


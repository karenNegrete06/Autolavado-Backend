
from Models.model_servicio_vehiculo import ServicioVehiculo
from Models.model_vehiculo import Vehiculo
import Schemas.schema_vehiculo
from sqlalchemy.orm import Session

def get_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vehiculo).offset(skip).limit(limit).all()

def get_vehiculo_by_id(db: Session, au_id: int):
    return db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()

def create_vehiculo(db: Session, vehiculo: Schemas.schema_vehiculo.VehiculoCreate):
    db_vehiculo = Vehiculo(
        au_modelo=vehiculo.au_modelo,
        au_matricula=vehiculo.au_matricula,
        au_color=vehiculo.au_color,
        au_tipo=vehiculo.au_tipo,
        au_usuario_id=vehiculo.au_usuario_id,
        cl_id=vehiculo.cl_id
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, au_id: int, vehiculo: Schemas.schema_vehiculo.VehiculoCreate):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()
    if db_vehiculo is None:
        return None
    db_vehiculo.au_matricula = vehiculo.au_matricula
    db_vehiculo.au_tipo = vehiculo.au_tipo
    db_vehiculo.au_color = vehiculo.au_color
    db_vehiculo.au_modelo = vehiculo.au_modelo
    db_vehiculo.au_usuario_id = vehiculo.au_usuario_id
    db_vehiculo.cl_id = vehiculo.cl_id

    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, au_id: int):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()
    if db_vehiculo is None:
        return None
    db.delete(db_vehiculo)
    db.commit()
    return db_vehiculo

def get_vehiculo_by_marca(db: Session, au_marca: str):
    return db.query(Vehiculo).filter(Vehiculo.au_marca == au_marca).first()

def get_vehiculo_by_modelo(db: Session, au_modelo: str):
    return db.query(Vehiculo).filter(Vehiculo.au_modelo == au_modelo).first()

def get_vehiculo_by_anio(db: Session, au_anio: int):
    return db.query(Vehiculo).filter(Vehiculo.au_anio == au_anio).first()

def get_vehiculo_by_color(db: Session, au_color: str):
    return db.query(Vehiculo).filter(Vehiculo.au_color == au_color).first()


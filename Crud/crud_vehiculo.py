
from Models.model_servicio_vehiculo import ServicioVehiculo
from Models.model_vehiculo import Vehiculo
import Schemas.schema_vehiculo
from sqlalchemy.orm import Session

def get_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vehiculo).offset(skip).limit(limit).all()

def get_vehiculo_by_matricula(db: Session, matricula: str):
    return db.query(Vehiculo).filter(Vehiculo.au_matricula == matricula).first()

def get_vehiculo_by_id(db: Session, au_id: int):
    return db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()

def create_vehiculo(db: Session, vehiculo: Schemas.schema_vehiculo.VehiculoCreate):
    db_vehiculo = Vehiculo(
        au_usuario_id=vehiculo.au_usuario_id,
        au_matricula=vehiculo.au_matricula,
        au_marca=vehiculo.au_marca,
        au_modelo=vehiculo.au_modelo,
        au_anio=vehiculo.au_anio,
        au_color=vehiculo.au_color,
        au_tipo=vehiculo.au_tipo,
        au_serie=vehiculo.au_serie,
        au_estado=vehiculo.au_estado,
        fecha_registro=vehiculo.fecha_registro,
        fecha_modificacion=vehiculo.fecha_modificacion
        
        
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, au_id: int, vehiculo: Schemas.schema_vehiculo.VehiculoCreate):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()
    if db_vehiculo is None:
        for var, value in vars(vehiculo).items():
            setattr(db_vehiculo, var, value) if value else None
        db.add(db_vehiculo)
        db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, au_id: int):
    db_vehiculo = db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()
    if db_vehiculo is None:
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


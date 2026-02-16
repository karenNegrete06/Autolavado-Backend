import Models.model_user
import Schemas.schema_user
from sqlalchemy.orm import Session

def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.model_user.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(Models.model_user.User).filter(Models.model_user.User.user_id == user_id).first()

def create_user(db: Session, user: Schemas.schema_user.UserCreate):
    db_user = Models.model_user.User(
        user_nombre=user.user_nombre,
        user_apellido=user.user_apellido,
        user_email=user.user_email,
        user_password=user.user_password,
        user_estado=user.user_estado,
        fecha_registro=user.fecha_registro,
        fecha_modificacion=user.fecha_modificacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: Schemas.schema_user.UserCreate):
    db_user = db.query(Models.model_user.User).filter(Models.model_user.User.user_id == user_id).first()
    if db_user is None:
        return None
    db_user.user_nombre = user.user_nombre
    db_user.user_apellido = user.user_apellido
    db_user.user_email = user.user_email
    db_user.user_password = user.user_password
    db_user.user_estado = user.user_estado
    db_user.fecha_modificacion = user.fecha_modificacion
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(Models.model_user.User).filter(Models.model_user.User.user_id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def get_user_by_email(db: Session, user_email: str):
    return db.query(Models.model_user.User).filter(Models.model_user.User.user_email == user_email).first()


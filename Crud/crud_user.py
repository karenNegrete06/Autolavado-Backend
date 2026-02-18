
from Models.model_user import User
import Schemas.schema_user
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.exc import UnknownHashError


def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: Schemas.schema_user.UserCreate):
    password_plana=user.password.strip()
    hashed_password = pwd_context.hash(password_plana)
    db_user = User(
        rol_id=user.rol_id,
        nombre=user.nombre,
        papellido=user.papellido,
        sapellido=user.sapellido,
        usuario=user.usuario,
        password=hashed_password,
        direccion=user.direccion,
        telefono=user.telefono,
        correo=user.correo,
        estatus=user.estatus,
        fecha_registro=user.fecha_registro,
        fecha_modificacion=user.fecha_modificacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: Schemas.schema_user.UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    db_user.nombre = user.nombre
    db_user.papellido = user.papellido
    db_user.sapellido = user.sapellido
    db_user.usuario = user.usuario
    db_user.correo = user.correo
    db_user.estatus = user.estatus
    db_user.fecha_modificacion = user.fecha_modificacion
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter((User.usuario == username) | (User.password == password)).first()
    if not user:
        return None
    try:
        if pwd_context.verify(password, user.password):
            return user
    except UnknownHashError:
        print("Error: El hash de la contraseña no es reconocido.")
    return None

def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.correo == user_email).first()



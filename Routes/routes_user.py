from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from Config.security import get_current_user
import Config.db, Models.model_user, Schemas.schema_user, Crud.crud_user
from typing import List
from Config.security import create_access_token


user=APIRouter()

def get_db():
    db = Config.db.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@user.get("/user/", response_model=List[Schemas.schema_user.UserResponse], tags=["User"])
async def read_users(skip:int=0, limit: int = 10, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.get_user(db=db, skip=skip, limit=limit)
    return db_user

@user.post("/user/", response_model=Schemas.schema_user.UserResponse, tags=["User"])
def create_user(usuario: Schemas.schema_user.UserCreate, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.get_user_by_nombre(db, nombre=usuario.nombre)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return Crud.crud_user.create_user(db=db, usuario=usuario)



@user.put("/user/{user_id}", response_model=Schemas.schema_user.UserResponse, tags=["User"])
async def update_user(id: int, usuario: Schemas.schema_user.UserUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_user = Crud.crud_user.update_user(db=db, id=id, usuario=usuario)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_user

@user.delete("/user/{user_id}", tags=["User"])
async def delete_user(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_user = Crud.crud_user.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="El Usuario no existe, no se pudo eliminar")
    return db_user

@user.post("/login/",tags=["Login"])
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = Crud.crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    
    access_token = create_access_token(data={"sub": user.usuario})
    return {"access_token": access_token, "token_type": "bearer"}
    




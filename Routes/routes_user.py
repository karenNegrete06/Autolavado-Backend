from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import Config.db, Models.model_user, Schemas.schema_user, Crud.crud_user
from typing import List


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
async def create_user(user: Schemas.schema_user.UserCreate, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.create_user(db=db, user=user)
    return db_user

@user.get("/user/{user_id}", response_model=Schemas.schema_user.UserResponse, tags=["User"])
async def read_user(user_id: int, db: Session = Depends(get_db)): 
    db_user = Crud.crud_user.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return db_user

@user.put("/user/{user_id}", response_model=Schemas.schema_user.UserResponse, tags=["User"])
async def update_user(user_id: int, user: Schemas.schema_user.UserCreate, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return db_user

@user.delete("/user/{user_id}", tags=["User"])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return {"detail": "User eliminado exitosamente"}

@user.get("/user/email/{user_email}", response_model=Schemas.schema_user.UserResponse, tags=["User"])
async def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = Crud.crud_user.get_user_by_email(db=db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return db_user


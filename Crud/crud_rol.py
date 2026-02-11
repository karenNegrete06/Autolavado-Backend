import Models.model_rols
import Schemas.schema_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.model_rols).offeset(skip).limit(limit).all()
"""
Modelo Rol para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from Config.db import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    """
    Representa la tabla tbc_roles.
    """
    __tablename__ = "tbc_roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60))
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    
    usuarios = relationship("Usuario", back_populates="rols")

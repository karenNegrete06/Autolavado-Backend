"""
Modelo Usuario para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from Config.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    """
    Representa la tabla tbb_usuario.
    """
    __tablename__ = "tbb_usuario"

    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey("tbc_roles.id"), nullable=False)

    nombre = Column(String(60), nullable=False)
    papellido = Column(String(60), nullable=False)
    sapellido = Column(String(60), nullable=True)
    usuario = Column(String(60), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    direccion = Column(String(255), nullable=True)
    telefono = Column(String(20), nullable=True, unique=True)
    correo = Column(String(100), nullable=True, unique=True)

    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=func.now)
    fecha_modificacion = Column(DateTime, onupdate=func.now)
    
    rols = relationship("Rol", back_populates="usuarios")
    vehiculos = relationship("Vehiculo", back_populates="usuarios")
    servicios_cajero = relationship("ServicioVehiculo", back_populates="cajero", foreign_keys="ServicioVehiculo.cajero_id")
    servicios_operativo = relationship("ServicioVehiculo", back_populates="operativo", foreign_keys="ServicioVehiculo.operativo_id")

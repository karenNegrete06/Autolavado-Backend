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
    rol_id = Column(Integer, ForeignKey("tbc_roles.id"))
    nombre = Column(String(60))
    papellido = Column(String(60))
    sapellido = Column(String(60))
    password = Column(String(255))

    direccion = Column(String(255))
    telefono = Column(String(20))
    correo = Column(String(100))

    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    
    rols = relationship("Rol", back_populates="usuarios")
    vehiculos = relationship("Vehiculo", back_populates="usuarios")
    servicios_cajero = relationship("ServicioVehiculo", back_populates="cajero", foreign_keys="ServicioVehiculo.cajero_id")
    servicios_operativo = relationship("ServicioVehiculo", back_populates="operativo", foreign_keys="ServicioVehiculo.operativo_id")

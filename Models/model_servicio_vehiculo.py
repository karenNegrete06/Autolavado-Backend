"""
Modelo ServicioVehiculo para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import (
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
    Float,
    Time,
    Column,
    Enum as SQLEnum
)
from sqlalchemy.sql import func
from Config.db import Base
from enum import Enum as PyEnum
import Models.model_servicio
from sqlalchemy.orm import relationship

class Solicitud(PyEnum):
    Programado="Programado"
    Proceso="Proceso"
    Realizada="Realizada"
    Cancelada="Cancelada"

class ServicioVehiculo(Base):
    """
    Representa la tabla tbd_servicio_vehiculo.
    """
    __tablename__ = "tbd_servicio_vehiculo"

    as_id = Column(Integer, primary_key=True, index=True)

    au_id = Column(Integer, ForeignKey("tbb_vehiculo.au_id"), nullable=False)
    cajero_id =Column(Integer, ForeignKey("tbb_usuario.id"), nullable=False)
    operativo_id= Column(Integer, ForeignKey("tbb_usuario.id"), nullable=False)
    se_id = Column(Integer, ForeignKey("tbc_servicio.se_id"), nullable=False)
   

    as_fecha = Column(DateTime, default=func.now())
    as_hora = Column(Time, default=func.now())
    as_estatus = Column(SQLEnum(Solicitud, name="solicitud_enum"), default=Solicitud.Programado)
    as_estado = Column(Boolean)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_modificacion = Column(DateTime, onupdate=func.now())
    
    cajero = relationship("Usuario", back_populates="servicios_cajero", foreign_keys=[cajero_id])
    operativo = relationship("Usuario", back_populates="servicios_operativo", foreign_keys=[operativo_id])
    servicio = relationship("Servicio", back_populates="servicios_vehiculo")
    vehiculo = relationship("Vehiculo", back_populates="servicios_vehiculo")
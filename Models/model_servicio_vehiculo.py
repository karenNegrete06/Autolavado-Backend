"""
Modelo ServicioVehiculo para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods


from sqlalchemy import Column, Integer, Boolean, DateTime,Date,Time, ForeignKey,Enum 
import enum
from sqlalchemy.sql import func
from Config.db import Base
from enum import Enum as PyEnum
import Models.model_servicio
from sqlalchemy.orm import relationship

class Solicitud(str,enum.Enum):
    PROGRAMADA="Programada"
    PROCESO="Proceso"
    REALIZADA="Finalizada"
    CANCELADA="Cancelada"

class ServicioVehiculo(Base):
    """
    Representa la tabla tbd_servicio_vehiculo.
    """
    __tablename__ = "tbd_servicio_vehiculo"

    as_id = Column(Integer, primary_key=True, index=True)

    au_id = Column(Integer, ForeignKey("tbb_vehiculo.au_id"))
    cajero_id =Column(Integer, ForeignKey("tbb_usuario.id"))
    operativo_id= Column(Integer, ForeignKey("tbb_usuario.id"))
    se_id = Column(Integer, ForeignKey("tbc_servicio.se_id"))
   

    as_fecha = Column(Date)
    as_hora = Column(Time)
    as_estatus = Column(Enum(Solicitud), nullable=False)
    as_estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    
    cajero = relationship("Usuario", back_populates="servicios_cajero", foreign_keys=[cajero_id])
    operativo = relationship("Usuario", back_populates="servicios_operativo", foreign_keys=[operativo_id])
    servicio = relationship("Servicio", back_populates="servicios_vehiculo")
    vehiculo = relationship("Vehiculo", back_populates="servicios_vehiculo")
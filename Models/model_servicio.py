"""
Modelo Servicio para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from Config.db import Base
from sqlalchemy.orm import relationship

class Servicio(Base):
    """
    Representa la tabla tbc_servicio.
    """
    __tablename__ = "tbc_servicio"

    se_id = Column(Integer, primary_key=True, index=True)
    se_nombre = Column(String(80))
    se_descripcion = Column(String(850))
    se_precio = Column(Float)
    se_estatus = Column(Boolean)
    se_duracion_minutos=Column(Integer)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    
    servicios_vehiculo = relationship("ServicioVehiculo", back_populates="servicio")
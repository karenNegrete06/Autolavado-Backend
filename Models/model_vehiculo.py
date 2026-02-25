"""
Modelo Vehiculo para la base de datos.
"""
from sqlalchemy.orm import relationship
# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, ForeignKey
from Config.db import Base


class Vehiculo(Base):
    """
    Representa la tabla tbb_vehiculo.
    """
    __tablename__ = "tbb_vehiculo"

    au_id = Column(Integer, primary_key=True, index=True)
    au_usuario_id=Column(Integer, ForeignKey("tbb_usuario.id"))
    au_matricula = Column(String(45))
    au_marca= Column(String(45))
    au_modelo = Column(String(45))
    au_anio = Column(Integer)
    au_color = Column(String(45))
    au_tipo = Column(String(45))
    au_serie = Column(String(45))
    au_estado = Column(String(45))
    fecha_registro = Column(String(45))
    fecha_modificacion = Column(String(45))

    usuario = relationship("User", back_populates="vehiculos")
    servicios_vehiculo = relationship("ServicioVehiculo", back_populates="vehiculo")
"""
Modelo Vehiculo para la base de datos.
"""

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
    au_modelo = Column(String(45), nullable=False)
    au_matricula = Column(String(45), nullable=False, unique=True)
    au_color = Column(String(45), nullable=True)
    au_tipo = Column(String(45), nullable=True)
    au_usuario_id=Column(Integer, ForeignKey("tbb_usuario.id"))
    

    cl_id = Column(Integer, ForeignKey("tbb_usuario.id"), nullable=False)

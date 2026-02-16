from fastapi import FastAPI
from Config.db import Base, engine

# IMPORTAR TODOS LOS MODELOS (ANTES de create_all)
import Models.model_rols
import Models.model_user
import Models.model_servicio
import Models.model_servicio_vehiculo
import Models.model_vehiculo

from Routes.routes_rol import rol
from Routes.routes_user import user
from Routes.routes_servicio_vehiculo import servicio_vehiculo
from Routes.routes_servicio import servicio
from Routes.routes_vehiculo import vehiculo


app = FastAPI(
    title="Sistema de control de autolavado",
    description="Sistema de creacion y almacenamiento de informacion y ventas en un autolavado"
)

# 🔥 Crear tablas UNA SOLA VEZ
Base.metadata.create_all(bind=engine)

app.include_router(rol)
app.include_router(user)
app.include_router(servicio_vehiculo)
app.include_router(servicio)
app.include_router(vehiculo)

    




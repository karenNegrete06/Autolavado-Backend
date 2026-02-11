"""
Módulo principal de la API de usuarios.

Implementa una API REST con FastAPI que permite
crear, consultar, actualizar y eliminar usuarios
utilizando una base de datos simulada en memoria.
"""



from fastapi import FastAPI, HTTPException
from Routes.routes_rol import rol



app = FastAPI(
    title="Sistema de control de autolavado",
    descripcion="Sistema de creacion y almacenamiento de informacion y ventas en un autolavado"
)


app.include_router(rol)

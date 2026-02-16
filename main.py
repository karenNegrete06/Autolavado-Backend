"""
Módulo principal de la API de usuarios.

Implementa una API REST con FastAPI que permite
crear, consultar, actualizar y eliminar usuarios
utilizando una base de datos simulada en memoria.
"""



from fastapi import FastAPI, HTTPException
from Routes.routes_rol import rol
from Routes.routes_user import user
from Routes.routes_servicio_vehiculo import servicio_vehiculo
from Routes.routes_servicio import servicio
from Routes.routes_vehiculo import vehiculo





app = FastAPI(
    title="Sistema de control de autolavado",
    descripcion="Sistema de creacion y almacenamiento de informacion y ventas en un autolavado"
)



app.include_router(rol)
app.include_router(user)
app.include_router(servicio_vehiculo)
app.include_router(servicio)
app.include_router(vehiculo)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="", port=8000)

    




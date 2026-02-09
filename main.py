"""
Módulo principal de la API de usuarios.

Implementa una API REST con FastAPI que permite
crear, consultar, actualizar y eliminar usuarios
utilizando una base de datos simulada en memoria.
"""

from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from models.user import Usuario, Genero
from models.rol import Rol


app = FastAPI()

# Base de datos simulada
db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Manuel",
        apellido="Negrete",
        genero=Genero.MASCULINO,
        rol=[Rol.ADMIN]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Matias",
        apellido="Granillo",
        genero=Genero.MASCULINO,
        rol=[Rol.USER]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Angel",
        apellido="Rufino",
        genero=Genero.MASCULINO,
        rol=[Rol.USER]
    ),
]


@app.get("/")
async def root():
    """
    Ruta raíz de la API.

    Returns:
        dict: Mensaje de bienvenida.
    """
    return {"message": "Hola soy Ses"}


@app.get("/api/v1/usuarios", response_model=List[Usuario])
async def get_usuarios():
    """
    Obtiene la lista completa de usuarios.

    Returns:
        List[Usuario]: Lista de usuarios registrados.
    """
    return db


@app.get("/api/v1/usuarios/{usuario_id}", response_model=Usuario)
async def get_usuario(usuario_id: UUID):
    """
    Obtiene un usuario por su ID.

    Args:
        usuario_id (UUID): Identificador del usuario.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        Usuario: Usuario encontrado.
    """
    for usuario in db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.post("/api/v1/usuarios", response_model=Usuario)
async def crear_usuario(usuario: Usuario):
    """
    Crea un nuevo usuario.

    Args:
        usuario (Usuario): Datos del usuario a crear.

    Returns:
        Usuario: Usuario creado con ID asignado.
    """
    usuario.id = uuid4()
    db.append(usuario)
    return usuario


@app.put("/api/v1/usuarios/{usuario_id}", response_model=Usuario)
async def actualizar_usuario(usuario_id: UUID, usuario_actualizado: Usuario):
    """
    Actualiza un usuario existente.

    Args:
        usuario_id (UUID): ID del usuario a actualizar.
        usuario_actualizado (Usuario): Nuevos datos del usuario.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        Usuario: Usuario actualizado.
    """
    for index, usuario in enumerate(db):
        if usuario.id == usuario_id:
            usuario_actualizado.id = usuario_id
            db[index] = usuario_actualizado
            return usuario_actualizado
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.delete("/api/v1/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: UUID):
    """
    Elimina un usuario por su ID.

    Args:
        usuario_id (UUID): ID del usuario a eliminar.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        dict: Mensaje de confirmación.
    """
    for index, usuario in enumerate(db):
        if usuario.id == usuario_id:
            db.pop(index)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
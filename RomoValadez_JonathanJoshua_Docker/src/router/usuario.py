from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from database import database as connection
from database import Usuario

from schemas import UsuarioBaseModel, UsuarioResponseModel, UsuarioPutModel

router = APIRouter(
    prefix="/usuario",
    tags=["usuario"],
)

@router.get("/")
async def obtener_usuarios():
    usuarios = Usuario.select()
    usuarios = [usuario for usuario in usuarios]
    response = parse_obj_as(List[UsuarioResponseModel], usuarios)
    return response

@router.post("/")
async def crear_usuario(usuario: UsuarioBaseModel):
    if Usuario.select().where(Usuario.NombreUsuario == usuario.NombreUsuario).exists():
        raise HTTPException(409, 'El usuario ya se encuentra en uso.')

    #hash_contrasena = Usuario.create_contrasena(usuario.contrasena)

    usuario = Usuario.create(
        NombreUsuario = usuario.NombreUsuario,
        Contrasena = usuario.Contrasena
    )

    return {
        "ID Usuario" : usuario.IDUsuario
    }

@router.get("/{IDUsuario}")
async def obtener_usuario(IDUsuario: int):
    usuario = Usuario.select().where(Usuario.IDUsuario == IDUsuario).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    return usuario.__data__

@router.put("/{IDUsuario}")
async def actualizar_usuario(IDUsuario: int, usuario: UsuarioPutModel):
    usuarioActualizado = Usuario.select().where(Usuario.IDUsuario == IDUsuario).first()

    if usuarioActualizado is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    #hash_contrasena = Usuario.create_contrasena(usuarioActualizado.contrasena)

    usuarioActualizado.NombreUsuario = usuario.NombreUsuario
    usuarioActualizado.Constrasena = usuario.Contrasena

    usuarioActualizado.save()

    return {
        "ID usuario" : usuarioActualizado.IDUsuario
    }

@router.delete("/{IDUsuario}")
async def eliminar_usuario(IDUsuario: int):
    usuario = Usuario.select().where(Usuario.IDUsuario == IDUsuario).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    usuario.delete_instance()
    
    return {
        "status" : "ok"
    }
from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from router import inicio_sesion

from database import database as connection
from database import Administrador

from schemas import AdministradorBaseModel, AdministradorResponseModel, AdministradorPutModel

router = APIRouter(
    prefix="/administrador",
    tags=["administrador"],
)

manager = inicio_sesion.manager


@router.get("/")
async def obtener_administradores():
    administradores = Administrador.select()
    administradores = [administrador for administrador in administradores]
    response = parse_obj_as(List[AdministradorResponseModel], administradores)
    return response

@router.post("/")
async def crear_administrador(administrador: AdministradorBaseModel, admin=Depends(manager)):
    if Administrador.select().where(Administrador.Usuario == administrador.Usuario).exists():
        raise HTTPException(409, 'El usuario ya se encuentra en uso.')

    #hash_contrasena = Administrador.create_contrasena(administrador.contrasena)

    administrador = Administrador.create(
        NombreAdmin = administrador.NombreAdmin,
        ApellidoP = administrador.ApellidoP,
        ApellidoM = administrador.ApellidoM,
        Usuario = administrador.Usuario,
        Contrasena = administrador.Contrasena
    )

    return {
        "ID Administrador" : administrador.IDAdmin
    }

@router.get("/{IDAdmin}")
async def obtener_administrador(IDAdmin: int):
    administrador = Administrador.select().where(Administrador.IDAdmin == IDAdmin).first()

    if administrador is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    return administrador.__data__

@router.put("/{IDAdmin}")
async def actualizar_administrador(IDAdmin: int, administrador: AdministradorPutModel):
    administradorActualizado = Administrador.select().where(Administrador.IDAdmin == IDAdmin).first()

    if administradorActualizado is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    #hash_contrasena = Administrador.create_contrasena(administradorActualizado.contrasena)

    administradorActualizado.NombreAdmin = administrador.NombreAdmin
    administradorActualizado.ApellidoP = administrador.ApellidoP
    administradorActualizado.ApellidoM = administrador.ApellidoM
    administradorActualizado.Usuario = administrador.Usuario
    administradorActualizado.Constrasena = administrador.Contrasena

    administradorActualizado.save()

    return {
        "ID Administrador" : administradorActualizado.IDAdmin
    }

@router.delete("/{IDAdmin}")
async def eliminar_administrador(IDAdmin: int):
    administrador = Administrador.select().where(Administrador.IDAdmin == IDAdmin).first()

    if administrador is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    administrador.delete_instance()
    
    return {
        "status" : "ok"
    }
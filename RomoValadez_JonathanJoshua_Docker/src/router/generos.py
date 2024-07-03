from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from database import database as connection
from database import Generos

from schemas import GenerosBaseModel, GenerosResponseModel

router = APIRouter(
    prefix="/generos",
    tags=["generos"],
)

@router.get("/")
async def obtener_generos():
    generos = Generos.select()
    generos = [genero for genero in generos]
    response = parse_obj_as(List[GenerosResponseModel], generos)
    return response

@router.post("/")
async def crear_genero(genero: GenerosBaseModel):
    if Generos.select().where(Generos.Nombre == genero.Nombre).exists():
        raise HTTPException(409, 'El nombre ya se encuentra en uso.')

    genero = Generos.create(
        Nombre = genero.Nombre
    )

    return {
        "Nombre genero" : genero.Nombre
    }

@router.get("/{Nombre}")
async def obtener_genero(Nombre: str):
    genero = Generos.select().where(Generos.Nombre == Nombre).first()

    if genero is None:
        raise HTTPException(status_code=404, detail='Nombre no encontrado')
    
    return genero.__data__

@router.delete("/{Nombre}")
async def eliminar_genero(Nombre: str):
    genero = Generos.select().where(Generos.Nombre == Nombre).first()

    if genero is None:
        raise HTTPException(status_code=404, detail='Nombre no encontrado')
    
    genero.delete_instance()
    
    return {
        "status" : "ok"
    }
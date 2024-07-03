from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from database import database as connection
from database import Genero_Pelicula, Generos, Pelicula

from schemas import GeneroPeliculaBaseModel, GeneroPeliculaResponseModel

router = APIRouter(
    prefix="/genero_pelicula",
    tags=["genero_pelicula"],
)

@router.get("/")
async def obtener_generos_peliculas():
    generos_peliculas = Genero_Pelicula.select()
    generos_peliculas = [genero_pelicula for genero_pelicula in generos_peliculas]
    response = parse_obj_as(List[GeneroPeliculaResponseModel], generos_peliculas)
    return response


@router.post("/")
async def crear_genero_pelicula(genero_pelicula: GeneroPeliculaBaseModel):
    anterior = Genero_Pelicula.select().where((Genero_Pelicula.Nombre == genero_pelicula.Nombre) & (Genero_Pelicula.IDPelicula == genero_pelicula.IDPelicula)).first()
    
    if anterior is not None:
        raise HTTPException(409, 'Ya existe esta relacion')
    
    genero = Generos.select().where(Generos.Nombre == genero_pelicula.Nombre).first()

    if genero is None:
        raise HTTPException(status_code=404, detail='Genero no encontrado')
    
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == genero_pelicula.IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')

    genero_pelicula = Genero_Pelicula.create(
        Nombre = genero_pelicula.Nombre,
        IDPelicula = genero_pelicula.IDPelicula
    )

    return {
        "status" : "ok"
    }

@router.get("/{IDPelicula}")
async def obtener_genero_pelicula(IDPelicula: int):
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')

    generos_peliculas = Genero_Pelicula.select().where(Genero_Pelicula.IDPelicula == IDPelicula)
    generos_peliculas = [genero_pelicula for genero_pelicula in generos_peliculas]
    response = parse_obj_as(List[GeneroPeliculaResponseModel], generos_peliculas)

    
    return response

@router.delete("/{Nombre}/{IDPelicula}")
async def eliminar_genero_pelicula(Nombre: str, IDPelicula: int):
    genero_pelicula = Genero_Pelicula.select().where((Genero_Pelicula.Nombre == Nombre) & (Genero_Pelicula.IDPelicula == IDPelicula)).first()

    if genero_pelicula is None:
        raise HTTPException(status_code=404, detail='No se ha encontrado la relacion')
    
    genero_pelicula.delete_instance()
    
    return {
        "status" : "ok"
    }
from fastapi import APIRouter, HTTPException, File, Depends, UploadFile
from pydantic import parse_obj_as
from typing import List
from PIL import Image
import io

from database import database as connection
from database import Pelicula

from schemas import PeliculaBaseModel, PeliculaResponseModel, PeliculaPutModel

router = APIRouter(
    prefix="/pelicula",
    tags=["pelicula"],
)

@router.get("/")
async def obtener_peliculas():
    peliculas = Pelicula.select()
    peliculas = [pelicula for pelicula in peliculas]
    response = parse_obj_as(List[PeliculaResponseModel], peliculas)
    return response

@router.post("/")
async def crear_pelicula(pelicula: PeliculaBaseModel):
    pelicula = Pelicula.create(
        Nombre = pelicula.Nombre,
        Descripcion = pelicula.Descripcion,
        Director = pelicula.Director,
        ClasificacionEdad = pelicula.ClasificacionEdad,
        Enlace = pelicula.Enlace,
        NombreSerie = pelicula.NombreSerie
    )

    return {
        "ID Pelicula" : pelicula.IDPelicula
    }

@router.post("/{IDPelicula}")
async def crear_pelicula(IDPelicula: str, img: UploadFile = File(...)):
    if not Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).exists():
        return HTTPException(409, 'El ID de esta pelicula no existe.')

    data = await img.read()
    image = Image.open(io.BytesIO(data))
    image.save("static/" + IDPelicula + ".png")

    return "ok"

@router.get("/ID/{IDPelicula}")
async def obtener_pelicula(IDPelicula: int):
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    return pelicula.__data__

@router.get("/Nombre/{Nombre}")
async def obtener_pelicula_nombre(Nombre: str):
    peliculas = Pelicula.select().where(Pelicula.Nombre ** ('%' + Nombre + '%'))
    peliculas = [pelicula for pelicula in peliculas]
    response = parse_obj_as(List[PeliculaResponseModel], peliculas)
    return response

@router.put("/{IDPelicula}")
async def actualizar_pelicula(IDPelicula: int, pelicula: PeliculaPutModel):
    peliculaActualizada = Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).first()

    if peliculaActualizada is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')

    peliculaActualizada.Nombre = pelicula.Nombre
    peliculaActualizada.Descripcion = pelicula.Descripcion
    peliculaActualizada.Director = pelicula.Director
    peliculaActualizada.ClasificacionEdad = pelicula.ClasificacionEdad
    peliculaActualizada.Enlace = pelicula.Enlace
    peliculaActualizada.NombreSerie = pelicula.NombreSerie

    peliculaActualizada.save()
    return {
        "ID Pelicula" : peliculaActualizada.IDPelicula
    }

@router.delete("/{IDPelicula}")
async def eliminar_pelicula(IDPelicula: int):
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='ID no encontrado')
    
    pelicula.delete_instance()
    
    return {
        "status" : "ok"
    }
from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from database import database as connection
from database import Administrador_Pelicula, Administrador, Pelicula

from schemas import AdministradorPeliculaBaseModel, AdministradorPeliculaResponseModel

router = APIRouter(
    prefix="/administrador_pelicula",
    tags=["administrador_pelicula"],
)

@router.get("/")
async def obtener_administradores_peliculas():
    administradores_peliculas = Administrador_Pelicula.select()
    administradores_peliculas = [administrador_pelicula for administrador_pelicula in administradores_peliculas]
    response = parse_obj_as(List[AdministradorPeliculaResponseModel], administradores_peliculas)
    return response

@router.post("/")
async def crear_administrador_pelicula(administrador_pelicula: AdministradorPeliculaBaseModel):
    anterior = Administrador_Pelicula.select().where((Administrador_Pelicula.IDAdmin == administrador_pelicula.IDAdmin) & (Administrador_Pelicula.IDPelicula == administrador_pelicula.IDPelicula) & (Administrador_Pelicula.Fecha_y_Hora == administrador_pelicula.Fecha_y_Hora)).first()
    
    if anterior is not None:
        raise HTTPException(409, 'Ya existe esta relacion')
    
    administrador = Administrador.select().where(Administrador.IDAdmin == administrador_pelicula.IDAdmin).first()

    if administrador is None:
        raise HTTPException(status_code=404, detail='Administrador no encontrado')
    
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == administrador_pelicula.IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')

    administrador_pelicula = Administrador_Pelicula.create(
        IDAdmin = administrador_pelicula.IDAdmin,
        IDPelicula = administrador_pelicula.IDPelicula,
        Fecha_y_Hora = administrador_pelicula.Fecha_y_Hora
    )

    return {
        "status" : "ok"
    }

@router.get("/{IDPelicula}")
async def obtener_administrador_pelicula(IDPelicula: int):
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')

    administradores_peliculas = Administrador_Pelicula.select().where(Administrador_Pelicula.IDPelicula == IDPelicula)
    administradores_peliculas = [administrador_pelicula for administrador_pelicula in administradores_peliculas]
    response = parse_obj_as(List[AdministradorPeliculaResponseModel], administradores_peliculas)

    
    return response
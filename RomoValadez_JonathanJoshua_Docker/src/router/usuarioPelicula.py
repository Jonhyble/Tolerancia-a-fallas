from fastapi import APIRouter, HTTPException, Depends
from pydantic import parse_obj_as
from typing import List

from router import inicio_sesion

from database import database as connection
from database import Usuario_Pelicula, Usuario, Pelicula

from schemas import UsuarioPeliculaBaseModel, UsuarioPeliculaResponseModel

router = APIRouter(
    prefix="/usuario_pelicula",
    tags=["usuario_pelicula"],
)

manager = inicio_sesion.managerUsuario


@router.post("/")
async def crear_usuario_pelicula(usuario_pelicula: UsuarioPeliculaBaseModel, IDUsuario=Depends(manager)):
    anterior = Usuario_Pelicula.select().where((Usuario_Pelicula.IDUsuario == IDUsuario) & (Usuario_Pelicula.IDPelicula == usuario_pelicula.IDPelicula)).first()
    
    if anterior is not None:
        raise HTTPException(409, 'Ya existe esta relacion')
    
    usuario = Usuario.select().where(Usuario.IDUsuario == IDUsuario).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    
    pelicula = Pelicula.select().where(Pelicula.IDPelicula == usuario_pelicula.IDPelicula).first()

    if pelicula is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada')

    usuario_pelicula = Usuario_Pelicula.create(
        IDUsuario = IDUsuario,
        IDPelicula = usuario_pelicula.IDPelicula
    )

    return {
        "status" : "ok"
    }

@router.get("/")
async def obtener_usuario_pelicula(IDUsuario=Depends(manager)):
    usuario = Usuario.select().where(Usuario.IDUsuario == IDUsuario).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')

    usuarios_peliculas = Usuario_Pelicula.select().where(Usuario_Pelicula.IDUsuario == IDUsuario)
    usuarios_peliculas = [usuario_pelicula for usuario_pelicula in usuarios_peliculas]
    response = parse_obj_as(List[UsuarioPeliculaResponseModel], usuarios_peliculas)

    
    return response

@router.delete("/{IDPelicula}")
async def eliminar_usuario_pelicula(IDPelicula: int, IDUsuario=Depends(manager)):
    usuario_pelicula = Usuario_Pelicula.select().where((Usuario_Pelicula.IDUsuario == IDUsuario) & (Usuario_Pelicula.IDPelicula == IDPelicula)).first()

    if usuario_pelicula is None:
        raise HTTPException(status_code=404, detail='No se ha encontrado la relacion')
    
    usuario_pelicula.delete_instance()
    
    return {
        "status" : "ok"
    }
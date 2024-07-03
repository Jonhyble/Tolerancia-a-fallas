from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from datetime import timedelta

from database import database as connection
from database import Administrador
from database import Usuario

from schemas import InicioSesionAdministradorBaseModel, InicioSesionUsuarioBaseModel


router = APIRouter(
    prefix="/sesion",
    tags=["sesion"],
)

SECRET = "cisco123"
SECRET2 = "cisco321"

manager = LoginManager(SECRET, token_url='/login')

managerUsuario = LoginManager(SECRET2, token_url='/login/usuario')

@manager.user_loader()
async def load_user(Usuario: str):
    administrador = Administrador.select().where(Administrador.Usuario == Usuario).first()
    
    if administrador is None:
        raise InvalidCredentialsException
    
    return administrador.IDAdmin

@router.post("/login")
async def login(sesion: InicioSesionAdministradorBaseModel):
    administrador = Administrador.select().where((Administrador.Usuario == sesion.Usuario) & (Administrador.Contrasena == sesion.Contrasena)).first()

    if administrador is None:
        raise InvalidCredentialsException
    
    
    access_token = manager.create_access_token(
        data=dict(sub=administrador.Usuario),
        expires = timedelta(hours=12)
    )


    return {'access_token' : access_token, 'Usuario' : administrador.Usuario}

@router.get("/")
async def root(user=Depends(manager)):
    return {"message": "Hello World Admin"}


@managerUsuario.user_loader()
async def load_Usuario(NombreUsuario: str):
    usuario = Usuario.select().where(Usuario.NombreUsuario == NombreUsuario).first()
    
    if usuario is None:
        raise InvalidCredentialsException

    return usuario.IDUsuario

@router.post("/login/usuario")
async def login_Usuario(sesion: InicioSesionUsuarioBaseModel):
    usuario = Usuario.select().where((Usuario.NombreUsuario == sesion.NombreUsuario) & (Usuario.Contrasena == sesion.Contrasena)).first()

    if usuario is None:
        raise InvalidCredentialsException
    
    access_token = managerUsuario.create_access_token(
        data=dict(sub=usuario.NombreUsuario),
        expires = timedelta(days=7)
    )

    return {'access_token' : access_token, 'NombreUsuario' : usuario.NombreUsuario}

@router.get("/usuario")
async def root(user=Depends(managerUsuario)):
    return {"message": "Hello World"}
from pydantic import BaseModel, validator
from typing import Optional, Any
from datetime import datetime, date
from peewee import ModelSelect
from datetime import datetime

from pydantic.utils import GetterDict

"""

██████╗░░█████╗░░██████╗████████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██████╔╝██║░░██║╚█████╗░░░░██║░░░
██╔═══╝░██║░░██║░╚═══██╗░░░██║░░░
██║░░░░░╚█████╔╝██████╔╝░░░██║░░░
╚═╝░░░░░░╚════╝░╚═════╝░░░░╚═╝░░░
"""

class AdministradorBaseModel(BaseModel):
    NombreAdmin: str
    ApellidoP: str
    ApellidoM: Optional[str]
    Usuario: str
    Contrasena: str

    @validator('NombreAdmin')
    def nombre_validator(cls, NombreAdmin):
        if len(NombreAdmin) < 3 or len(NombreAdmin) > 30:
            raise ValueError("La longitud de los nombres se debe de encontrar entre los 3 y 30 caracteres")

        return NombreAdmin

    @validator('ApellidoP')
    def ApellidoP_validator(cls, ApellidoP):
        if len(ApellidoP) < 3 or len(ApellidoP) > 15:
            raise ValueError("La longitud del apellido paterno se debe de encontrar entre los 3 y 15 caracteres")

        return ApellidoP
    
    @validator('ApellidoM')
    def ApellidoM_validator(cls, ApellidoM):
        if ApellidoM is not None:
            if len(ApellidoM) < 3 or len(ApellidoM) > 15:
                raise ValueError("La longitud del apellido materno se debe de encontrar entre los 3 y 15 caracteres")

        return ApellidoM

    @validator('Usuario')
    def Usuario_validator(cls, Usuario):
        if len(Usuario) < 3 or len(Usuario) > 15:
            raise ValueError("La longitud del nombre de usuario se debe de encontrar entre los 3 y 15 caracteres")

        return Usuario
    
    @validator('Contrasena')
    def Contrasena_validator(cls, Contrasena):
        if len(Contrasena) < 3 or len(Contrasena) > 20:
            raise ValueError("La longitud de la contraseña se debe de encontrar entre los 3 y 20 caracteres")

        return Contrasena

class PeliculaBaseModel(BaseModel):
    Nombre: str
    Descripcion: str
    Director: str
    ClasificacionEdad: int
    Enlace: str
    NombreSerie: Optional[str]

    @validator('Nombre')
    def nombre_validator(cls, Nombre):
        if len(Nombre) < 3 or len(Nombre) > 40:
            raise ValueError("La longitud del nombre se debe de encontrar entre los 3 y 40 caracteres")

        return Nombre

    @validator('Descripcion')
    def descripcion_validator(cls, Descripcion):
        if len(Descripcion) < 3 or len(Descripcion) > 60:
            raise ValueError("La longitud de la descripcion se debe de encontrar entre los 3 y 60 caracteres")

        return Descripcion
    
    @validator('Director')
    def director_validator(cls, Director):
        if len(Director) < 3 or len(Director) > 40:
            raise ValueError("La longitud del nombre del director se debe de encontrar entre los 3 y 40 caracteres")

        return Director

    @validator('ClasificacionEdad')
    def clasificacionEdad_validator(cls, ClasificacionEdad):
        if ClasificacionEdad < 2 or ClasificacionEdad > 18:
            raise ValueError("La clasificacion de edad se debe de encontrar entre los 2 y 18 años")

        return ClasificacionEdad
    
    @validator('Enlace')
    def enlace_validator(cls, Enlace):
        if len(Enlace) < 10 or len(Enlace) > 250:
            raise ValueError("La longitud del enlace se debe de encontrar entre los 10 y 250 caracteres")

        return Enlace
    
    @validator('NombreSerie')
    def nombreSerie_validator(cls, NombreSerie):
        if len(NombreSerie) < 3 or len(NombreSerie) > 40:
            raise ValueError("La longitud del nombre de la serie se debe de encontrar entre los 3 y 40 caracteres")

        return NombreSerie

class UsuarioBaseModel(BaseModel):
    NombreUsuario: str
    Contrasena: str

    @validator('NombreUsuario')
    def NombreUsuario_validator(cls, NombreUsuario):
        if len(NombreUsuario) < 3 or len(NombreUsuario) > 15:
            raise ValueError("La longitud del nombre de usuario se debe de encontrar entre los 3 y 15 caracteres")

        return NombreUsuario
    
    @validator('Contrasena')
    def Contrasena_validator(cls, Contrasena):
        if len(Contrasena) < 3 or len(Contrasena) > 20:
            raise ValueError("La longitud de la contraseña se debe de encontrar entre los 3 y 20 caracteres")

        return Contrasena

class GenerosBaseModel(BaseModel):
    Nombre: str

    @validator('Nombre')
    def nombre_validator(cls, Nombre):
        if len(Nombre) < 3 or len(Nombre) > 20:
            raise ValueError("La longitud del nombre se debe de encontrar entre los 3 y 20 caracteres")

        return Nombre

class UsuarioPeliculaBaseModel(BaseModel):
    IDPelicula: int

class AdministradorPeliculaBaseModel(BaseModel):
    IDAdmin: int
    IDPelicula: int
    Fecha_y_Hora: datetime

class GeneroPeliculaBaseModel(BaseModel):
    Nombre: str
    IDPelicula: int

class InicioSesionAdministradorBaseModel(BaseModel):
    Usuario: str
    Contrasena: str

class InicioSesionUsuarioBaseModel(BaseModel):
    NombreUsuario: str
    Contrasena: str

""" 

██████╗░███████╗░██████╗██████╗░░█████╗░███╗░░██╗░██████╗███████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝
██████╔╝█████╗░░╚█████╗░██████╔╝██║░░██║██╔██╗██║╚█████╗░█████╗░░
██╔══██╗██╔══╝░░░╚═══██╗██╔═══╝░██║░░██║██║╚████║░╚═══██╗██╔══╝░░
██║░░██║███████╗██████╔╝██║░░░░░╚█████╔╝██║░╚███║██████╔╝███████╗
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝ 
"""


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        
        if isinstance(res, ModelSelect):
            return list(res)

        return res


class AdministradorResponseModel(BaseModel):
    IDAdmin: int
    NombreAdmin: str
    ApellidoP: str
    ApellidoM: Optional[str]
    Usuario: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class PeliculaResponseModel(BaseModel):
    IDPelicula: int
    Nombre: str
    Descripcion: str
    Director: str
    ClasificacionEdad: int
    Enlace: str
    NombreSerie: Optional[str]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class UsuarioResponseModel(BaseModel):
    IDUsuario: int
    NombreUsuario: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class GenerosResponseModel(BaseModel):
    Nombre: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class ReferenciaPeliculaResponseModel(BaseModel):
    IDPelicula: int
    Nombre: str
    NombreSerie: Optional[str]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class UsuarioPeliculaResponseModel(BaseModel):
    IDUsuario: UsuarioResponseModel
    IDPelicula: ReferenciaPeliculaResponseModel

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class AdministradorPeliculaResponseModel(BaseModel):
    IDAdmin: AdministradorResponseModel
    IDPelicula: ReferenciaPeliculaResponseModel
    Fecha_y_Hora: datetime

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class GeneroPeliculaResponseModel(BaseModel):
    Nombre: GenerosResponseModel
    IDPelicula: ReferenciaPeliculaResponseModel

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

"""

██████╗░██╗░░░██╗████████╗
██╔══██╗██║░░░██║╚══██╔══╝
██████╔╝██║░░░██║░░░██║░░░
██╔═══╝░██║░░░██║░░░██║░░░
██║░░░░░╚██████╔╝░░░██║░░░
╚═╝░░░░░░╚═════╝░░░░╚═╝░░░
"""


class AdministradorPutModel(BaseModel):
    NombreAdmin: str
    ApellidoP: str
    ApellidoM: Optional[str]
    Usuario: str
    Contrasena: str

    @validator('NombreAdmin')
    def nombre_validator(cls, NombreAdmin):
        if len(NombreAdmin) < 3 or len(NombreAdmin) > 30:
            raise ValueError("La longitud de los nombres se debe de encontrar entre los 3 y 30 caracteres")

        return NombreAdmin

    @validator('ApellidoP')
    def ApellidoP_validator(cls, ApellidoP):
        if len(ApellidoP) < 3 or len(ApellidoP) > 15:
            raise ValueError("La longitud del apellido paterno se debe de encontrar entre los 3 y 15 caracteres")

        return ApellidoP
    
    @validator('ApellidoM')
    def ApellidoM_validator(cls, ApellidoM):
        if ApellidoM is not None:
            if len(ApellidoM) < 3 or len(ApellidoM) > 15:
                raise ValueError("La longitud del apellido materno se debe de encontrar entre los 3 y 15 caracteres")

        return ApellidoM

    @validator('Usuario')
    def Usuario_validator(cls, Usuario):
        if len(Usuario) < 3 or len(Usuario) > 15:
            raise ValueError("La longitud del nombre de usuario se debe de encontrar entre los 3 y 15 caracteres")

        return Usuario
    
    @validator('Contrasena')
    def Contrasena_validator(cls, Contrasena):
        if len(Contrasena) < 3 or len(Contrasena) > 20:
            raise ValueError("La longitud de la contraseña se debe de encontrar entre los 3 y 20 caracteres")

        return Contrasena

class PeliculaPutModel(BaseModel):
    Nombre: str
    Descripcion: str
    Director: str
    ClasificacionEdad: int
    Enlace: str
    NombreSerie: Optional[str]

    @validator('Nombre')
    def nombre_validator(cls, Nombre):
        if len(Nombre) < 3 or len(Nombre) > 40:
            raise ValueError("La longitud del nombre se debe de encontrar entre los 3 y 40 caracteres")

        return Nombre

    @validator('Descripcion')
    def descripcion_validator(cls, Descripcion):
        if len(Descripcion) < 3 or len(Descripcion) > 60:
            raise ValueError("La longitud de la descripcion se debe de encontrar entre los 3 y 60 caracteres")

        return Descripcion
    
    @validator('Director')
    def director_validator(cls, Director):
        if len(Director) < 3 or len(Director) > 40:
            raise ValueError("La longitud del nombre del director se debe de encontrar entre los 3 y 40 caracteres")

        return Director

    @validator('ClasificacionEdad')
    def clasificacionEdad_validator(cls, ClasificacionEdad):
        if ClasificacionEdad < 2 or ClasificacionEdad > 18:
            raise ValueError("La clasificacion de edad se debe de encontrar entre los 2 y 18 años")

        return ClasificacionEdad
    
    @validator('Enlace')
    def enlace_validator(cls, Enlace):
        if len(Enlace) < 10 or len(Enlace) > 250:
            raise ValueError("La longitud del enlace se debe de encontrar entre los 10 y 250 caracteres")

        return Enlace
    
    @validator('NombreSerie')
    def nombreSerie_validator(cls, NombreSerie):
        if len(NombreSerie) < 3 or len(NombreSerie) > 40:
            raise ValueError("La longitud del nombre de la serie se debe de encontrar entre los 3 y 40 caracteres")

        return NombreSerie

class UsuarioPutModel(BaseModel):
    NombreUsuario: str
    Contrasena: str

    @validator('NombreUsuario')
    def NombreUsuario_validator(cls, NombreUsuario):
        if len(NombreUsuario) < 3 or len(NombreUsuario) > 15:
            raise ValueError("La longitud del nombre de usuario se debe de encontrar entre los 3 y 15 caracteres")

        return NombreUsuario
    
    @validator('Contrasena')
    def Contrasena_validator(cls, Contrasena):
        if len(Contrasena) < 3 or len(Contrasena) > 20:
            raise ValueError("La longitud de la contraseña se debe de encontrar entre los 3 y 20 caracteres")

        return Contrasena
    
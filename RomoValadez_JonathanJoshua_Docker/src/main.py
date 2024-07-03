from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import database as connection

from database import Administrador, Pelicula, Usuario, Generos, Usuario_Pelicula, Administrador_Pelicula, Genero_Pelicula

from router import administrador
from router import pelicula
from router import usuario
from router import generos
from router import usuarioPelicula
from router import administradorPelicula
from router import generoPelicula
from router import inicio_sesion

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#router
app.include_router(administrador.router)
app.include_router(pelicula.router)
app.include_router(usuario.router)
app.include_router(generos.router)
app.include_router(usuarioPelicula.router)
app.include_router(administradorPelicula.router)
app.include_router(generoPelicula.router)
app.include_router(inicio_sesion.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([  Administrador,
                                Pelicula,
                                Usuario,
                                Generos,
                                Usuario_Pelicula,
                                Administrador_Pelicula,
                                Genero_Pelicula])
    print("Bonjour")


@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()
    print("Arrive Derchi")


@app.get("/")
async def root():
    return {"message": "Hello World"}
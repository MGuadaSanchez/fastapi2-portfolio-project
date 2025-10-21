"""
Punto de entrada principal de la aplicación FastAPI.

Este módulo es responsable de:
- Crear la instancia de la aplicación FastAPI.
- Inicializar la base de datos y crear las tablas.
- Incluir los routers de los diferentes recursos.
- Montar los directorios de ficheros estáticos y plantillas.
"""
from fastapi import FastAPI, Request
from app.routers.movie_router import movie_router
from app.utils.http_error_handler import HTTPErrorHandler

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# --- Importaciones para la base de datos ---
from app.database import engine
from app.models import movie_model
# -----------------------------------------

        
app = FastAPI()

# --- Creación de la tabla en la base de datos ---
movie_model.Base.metadata.create_all(bind=engine)
# ---------------------------------------------


app.title = "Mi app con FastAPI"
app.version = "2.0.0"

app.add_middleware(HTTPErrorHandler)

static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount('/static', StaticFiles(directory=static_path), 'static')
templates = Jinja2Templates(directory=templates_path)

@app.get('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'message': 'Welcome'})

app.include_router(prefix='/movies', router=movie_router)
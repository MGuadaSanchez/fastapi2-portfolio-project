# API de Películas con FastAPI

Este repositorio contiene una API REST para gestionar un catálogo de películas, desarrollada con Python y FastAPI. El proyecto sigue una arquitectura limpia y modular, ideal como base para proyectos backend más complejos.

## Tecnologías Utilizadas

*   **Python 3.11+**
*   **FastAPI:** Framework web de alto rendimiento para construir APIs.
*   **Pydantic:** Para la validación y serialización de datos.
*   **SQLAlchemy:** ORM para la interacción con la base de datos.
*   **SQLite:** Base de datos SQL ligera basada en ficheros.
*   **Uvicorn:** Servidor ASGI para ejecutar la aplicación.

## Estructura del Proyecto

El proyecto sigue una arquitectura con separación de responsabilidades:

```
/FastAPI2
│
├── .gitignore          # Ficheros y carpetas ignorados por Git.
├── README.md           # Documentación del proyecto.
├── requirements.txt    # Lista de dependencias de Python.
├── movies.db           # Fichero de la base de datos (ignorado por Git).
├── venv/               # Entorno virtual.
│
└── app/                # Carpeta principal con el código fuente de la aplicación.
    ├── __init__.py
    ├── main.py             # Punto de entrada de la aplicación FastAPI.
    ├── database.py         # Configuración de la conexión a la base de datos.
    ├── dependencies.py     # Dependencias reutilizables (ej. sesión de DB).
    │
    ├── models/             # Modelos de la base de datos (SQLAlchemy).
    │   └── movie_model.py
    │
    ├── schemas/            # Esquemas de datos para la API (Pydantic).
    │   └── movie_schema.py
    │
    ├── services/           # Lógica de negocio de la aplicación.
    │   └── movie_service.py
    │
    ├── routers/            # Endpoints de la API.
    │   └── movie_router.py
    │
    └── utils/              # Utilidades y middlewares.
        └── http_error_handler.py
```

## Instrucciones de Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/MGuadaSanchez/fastapi2-portfolio-project.git
cd fastapi2-portfolio-project
```

### 2. Crear y activar el entorno virtual
```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/macOS
source venv/bin/activate
```

### 3. Instalar dependencias
Asegúrate de que tu entorno virtual está activado y luego ejecuta:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el proyecto
Para iniciar el servidor de desarrollo, ejecuta:
```bash
uvicorn app.main:app --reload
```
El servidor estará disponible en `http://127.0.0.1:8000`.

### 5. Probar la API
Puedes acceder a la documentación interactiva de la API (Swagger UI) para probar los endpoints en:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Autor

**Guadalupe Sanchez**

*   **GitHub:** [MGuadaSanchez](https://github.com/MGuadaSanchez)
*   **LinkedIn:** `(añade aquí tu enlace a LinkedIn)`

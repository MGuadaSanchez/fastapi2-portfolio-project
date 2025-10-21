"""
Define las dependencias reutilizables para la aplicación FastAPI.

Estas dependencias se pueden inyectar en los endpoints para proporcionar
funcionalidades comunes, como el acceso a la base de datos.
"""
from app.database import SessionLocal

def get_db():
    """
    Generador de sesión de base de datos para inyección de dependencias.

    Crea una nueva sesión de SQLAlchemy para cada petición, la proporciona
    al endpoint y se asegura de que se cierre correctamente al final.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()